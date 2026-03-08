import os
import json
import pandas as pd
import mysql.connector

path = "data/aggregated/user/country/india/state"

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
                
                try:
                    for item in content["data"]["usersByDevice"]:
                        
                        brand = item["brand"]
                        count = item["count"]
                        percentage = item["percentage"]
                        
                        data.append([
                            state,
                            year,
                            file.replace(".json",""),
                            brand,
                            count,
                            percentage
                        ])
                except:
                    pass

df = pd.DataFrame(data, columns=[
    "State",
    "Year",
    "Quarter",
    "Brand",
    "Count",
    "Percentage"
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
    
    sql = """INSERT INTO aggregated_user
    (state,year,quarter,brand,count,percentage)
    VALUES (%s,%s,%s,%s,%s,%s)"""
    
    values = (
        row["State"],
        int(row["Year"]),
        int(row["Quarter"]),
        row["Brand"],
        int(row["Count"]),
        float(row["Percentage"])
    )
    
    cursor.execute(sql,values)

connection.commit()

print("User data inserted successfully!")