import os
import json
import pandas as pd
import mysql.connector

path = "data/map/transaction/hover/country/india/state"

data = []

for state in os.listdir(path):
    state_path = path + "/" + state
    
    for year in os.listdir(state_path):
        year_path = state_path + "/" + year
        
        for file in os.listdir(year_path):
            
            if file.endswith(".json"):
                
                file_path = year_path + "/" + file
                
                with open(file_path) as f:
                    content = json.load(f)
                
                for item in content["data"]["hoverDataList"]:
                    
                    district = item["name"]
                    count = item["metric"][0]["count"]
                    amount = item["metric"][0]["amount"]
                    
                    data.append([
                        state,
                        year,
                        file.replace(".json",""),
                        district,
                        count,
                        amount
                    ])

df = pd.DataFrame(data, columns=[
    "State",
    "Year",
    "Quarter",
    "District",
    "Transaction_count",
    "Transaction_amount"
])

print(df.head())

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="720767",
    database="phonepe"
)

cursor = connection.cursor()

for i,row in df.iterrows():
    
    sql = """INSERT INTO map_transaction
    (state,year,quarter,district,transaction_count,transaction_amount)
    VALUES (%s,%s,%s,%s,%s,%s)"""
    
    values = (
        row["State"],
        int(row["Year"]),
        int(row["Quarter"]),
        row["District"],
        int(row["Transaction_count"]),
        float(row["Transaction_amount"])
    )
    
    cursor.execute(sql,values)

connection.commit()

print("Map transaction data inserted successfully!")