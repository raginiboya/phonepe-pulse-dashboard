import os
import json
import pandas as pd
import mysql.connector

# Correct dataset path
path = "data/map/user/hover/country/india/state"

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

                for district, info in content["data"]["hoverData"].items():

                    registered_users = info["registeredUsers"]
                    app_opens = info["appOpens"]

                    data.append([
                        state,
                        year,
                        file.replace(".json",""),
                        district,
                        registered_users,
                        app_opens
                    ])

df = pd.DataFrame(data, columns=[
    "State",
    "Year",
    "Quarter",
    "District",
    "Registered_users",
    "App_opens"
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

for i, row in df.iterrows():

    sql = """INSERT INTO map_user
    (state,year,quarter,district,registered_users,app_opens)
    VALUES (%s,%s,%s,%s,%s,%s)"""

    values = (
        row["State"],
        int(row["Year"]),
        int(row["Quarter"]),
        row["District"],
        int(row["Registered_users"]),
        int(row["App_opens"])
    )

    cursor.execute(sql, values)

connection.commit()

print("Map User data inserted successfully!")