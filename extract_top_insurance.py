import os
import json
import pandas as pd
import mysql.connector

# Dataset path
path = "data/top/insurance/country/india/state"

data = []

for state in os.listdir(path):

    state_path = os.path.join(path, state)

    for year in os.listdir(state_path):

        year_path = os.path.join(state_path, year)

        for file in os.listdir(year_path):

            if file.endswith(".json"):

                file_path = os.path.join(year_path, file)

                with open(file_path) as f:
                    content = json.load(f)

                try:
                    for item in content["data"]["pincodes"]:

                        pincode = item["entityName"]
                        count = item["metric"]["count"]
                        amount = item["metric"]["amount"]

                        data.append([
                            state,
                            year,
                            file.replace(".json",""),
                            pincode,
                            count,
                            amount
                        ])
                except:
                    pass


df = pd.DataFrame(data, columns=[
    "State",
    "Year",
    "Quarter",
    "Pincode",
    "Transaction_count",
    "Transaction_amount"
])

print(df.head())

# MySQL connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="720767",
    database="phonepe"
)

cursor = connection.cursor()

for i,row in df.iterrows():

    sql = """INSERT INTO top_insurance
    (state,year,quarter,pincode,transaction_count,transaction_amount)
    VALUES (%s,%s,%s,%s,%s,%s)"""

    values = (
        row["State"],
        int(row["Year"]),
        int(row["Quarter"]),
        0 if pd.isna(row["Pincode"]) else int(row["Pincode"]),
        int(row["Transaction_count"]),
        float(row["Transaction_amount"])
    )

    cursor.execute(sql,values)

connection.commit()

print("Top Insurance data inserted successfully!")