import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="720767",
    database="phonepe"
)

cursor = connection.cursor()

print("MySQL Connected Successfully!")

import pandas as pd

query = """
SELECT state,
SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10
"""

df = pd.read_sql(query, connection)

print(df)

query2 = """
SELECT brand,
AVG(percentage) AS avg_market_share
FROM aggregated_user
GROUP BY brand
ORDER BY avg_market_share DESC
"""

df2 = pd.read_sql(query2, connection)

print(df2)

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(8,8))

plt.pie(df2['avg_market_share'],
        labels=df2['brand'],
        autopct='%1.1f%%')

plt.title("Device Brand Market Share Distribution")

plt.show()

query3 = """
SELECT state,
brand,
SUM(count) AS total_users
FROM aggregated_user
GROUP BY state, brand
ORDER BY state, total_users DESC
"""

df3 = pd.read_sql(query3, connection)

print(df3)

pivot_df = df3.pivot(index="state", columns="brand", values="total_users")
pivot_df.plot(kind="bar", stacked=True, figsize=(12,7))

plt.title("Device Brand Usage Across States")
plt.xlabel("State")
plt.ylabel("Total Users")

plt.legend(title="Brand", bbox_to_anchor=(1.05,1))

plt.tight_layout()
plt.show()

query4 = """
SELECT year,
brand,
SUM(count) AS total_users
FROM aggregated_user
GROUP BY year, brand
ORDER BY year, total_users DESC
"""

df4 = pd.read_sql(query4, connection)

print(df4)

pivot_df4 = df4.pivot(index="year", columns="brand", values="total_users")
pivot_df4.plot(kind="line", marker="o", figsize=(10,6))

plt.title("Device Usage Growth Over Years")
plt.xlabel("Year")
plt.ylabel("Total Users")

plt.legend(title="Brand", bbox_to_anchor=(1.05,1))

plt.tight_layout()
plt.show()

query5 = """
SELECT year,
quarter,
brand,
SUM(count) AS total_users
FROM aggregated_user
GROUP BY year, quarter, brand
ORDER BY year, quarter
"""

df5 = pd.read_sql(query5, connection)

print(df5)

df5["year_quarter"] = df5["year"].astype(str) + "-Q" + df5["quarter"].astype(str)
pivot_df5 = df5.pivot(index="year_quarter", columns="brand", values="total_users")
pivot_df5.plot(marker="o", figsize=(12,6))

plt.title("Quarterly Device Engagement Trend")
plt.xlabel("Year-Quarter")
plt.ylabel("Total Users")

plt.xticks(rotation=45)

plt.legend(title="Brand", bbox_to_anchor=(1.05,1))

plt.tight_layout()
plt.show()

query6 = """
SELECT state,
SUM(transaction_amount) AS total_insurance_amount
FROM aggregated_insurance
GROUP BY state
ORDER BY total_insurance_amount DESC
LIMIT 10
"""

df6 = pd.read_sql(query6, connection)

print(df6)

plt.figure(figsize=(10,6))

sns.barplot(x="total_insurance_amount", y="state", data=df6)

plt.title("Top States by Insurance Transaction Amount")
plt.xlabel("Total Insurance Transaction Amount")
plt.ylabel("State")

plt.show()

query7 = """
SELECT state,
SUM(transaction_count) AS total_transactions
FROM aggregated_insurance
GROUP BY state
ORDER BY total_transactions DESC
LIMIT 10
"""

df7 = pd.read_sql(query7, connection)

print(df7)

plt.figure(figsize=(8,8))

plt.pie(df7['total_transactions'],
        labels=df7['state'],
        autopct='%1.1f%%',
        startangle=90)

# Create donut effect
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("States with Highest Insurance Transaction Volume")

plt.show()

query8 = """
SELECT year,
SUM(transaction_amount) AS yearly_insurance_amount
FROM aggregated_insurance
GROUP BY year
ORDER BY year
"""

df8 = pd.read_sql(query8, connection)

print(df8)

plt.figure(figsize=(10,6))

plt.fill_between(df8["year"], df8["yearly_insurance_amount"], alpha=0.4)

plt.plot(df8["year"], df8["yearly_insurance_amount"], marker="o")

plt.title("Yearly Insurance Transaction Growth")
plt.xlabel("Year")
plt.ylabel("Total Insurance Transaction Amount")

plt.show()

query9 = """
SELECT year,
quarter,
SUM(transaction_count) AS quarterly_transactions
FROM aggregated_insurance
GROUP BY year, quarter
ORDER BY year, quarter
"""

df9 = pd.read_sql(query9, connection)

print(df9)

pivot_df9 = df9.pivot(index="year", columns="quarter", values="quarterly_transactions")
plt.figure(figsize=(8,6))

sns.heatmap(pivot_df9, annot=True, fmt=".0f", cmap="YlGnBu")

plt.title("Quarterly Insurance Adoption Trend")
plt.xlabel("Quarter")
plt.ylabel("Year")

plt.show()

query10 = """
SELECT state,
year,
SUM(transaction_amount) AS total_amount
FROM aggregated_insurance
GROUP BY state, year
ORDER BY state, year
"""

df10 = pd.read_sql(query10, connection)

print(df10)

pivot_df10 = df10.pivot(index="year", columns="state", values="total_amount")
pivot_df10.plot(marker="o", figsize=(12,6))

plt.title("Insurance Adoption by State Over Time")
plt.xlabel("Year")
plt.ylabel("Total Insurance Transaction Amount")

plt.legend(title="State", bbox_to_anchor=(1.05,1))

plt.tight_layout()
plt.show()

query11 = """
SELECT state,
SUM(transaction_amount) AS total_transaction_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_transaction_amount DESC
LIMIT 10
"""

df11 = pd.read_sql(query11, connection)

print(df11)

plt.figure(figsize=(10,6))

sns.barplot(x="total_transaction_amount", y="state", data=df11)

plt.title("Top States by Total Transaction Amount")
plt.xlabel("Total Transaction Amount")
plt.ylabel("State")

plt.show()

query12 = """
SELECT state,
SUM(transaction_count) AS total_transactions
FROM aggregated_transaction
GROUP BY state
ORDER BY total_transactions DESC
LIMIT 10
"""

df12 = pd.read_sql(query12, connection)

print(df12)


import squarify

plt.figure(figsize=(10,6))

squarify.plot(
    sizes=df12["total_transactions"],
    label=df12["state"],
    alpha=0.8
)

plt.title("States with Highest Transaction Volume")
plt.axis("off")

plt.show()

query13 = """
SELECT year,
SUM(transaction_amount) AS yearly_transaction_amount
FROM aggregated_transaction
GROUP BY year
ORDER BY year
"""

df13 = pd.read_sql(query13, connection)

print(df13)

plt.figure(figsize=(10,6))

plt.plot(
    df13["year"],
    df13["yearly_transaction_amount"],
    marker='o'
)

plt.title("Yearly Transaction Growth")
plt.xlabel("Year")
plt.ylabel("Transaction Amount")
plt.grid(True)

plt.show()

query14 = """
SELECT year,
       quarter,
       SUM(transaction_amount) AS quarterly_amount
FROM aggregated_transaction
GROUP BY year, quarter
ORDER BY year, quarter
"""

df14 = pd.read_sql(query14, connection)

print(df14)

pivot_df = df14.pivot(index="quarter", columns="year", values="quarterly_amount")

print(pivot_df)
plt.figure(figsize=(10,6))

pivot_df.plot(marker='o')

plt.title("Quarterly Transaction Trends by Year")
plt.xlabel("Quarter")
plt.ylabel("Transaction Amount")
plt.grid(True)

plt.show()

query15 = """
SELECT transaction_type,
       SUM(transaction_count) AS total_transactions
FROM aggregated_transaction
GROUP BY transaction_type
ORDER BY total_transactions DESC
"""

df15 = pd.read_sql(query15, connection)

print(df15)

plt.figure(figsize=(10,6))

sns.barplot(
    x="total_transactions",
    y="transaction_type",
    data=df15
)

plt.title("Most Popular Transaction Types")
plt.xlabel("Total Transactions")
plt.ylabel("Transaction Type")

plt.show()

query16 = """
SELECT state,
       SUM(registered_users) AS total_users
FROM map_user
GROUP BY state
ORDER BY total_users DESC
LIMIT 10
"""

df16 = pd.read_sql(query16, connection)

print(df16)

plt.figure(figsize=(10,6))

sns.barplot(
    x="total_users",
    y="state",
    data=df16
)

plt.title("Top States by Registered PhonePe Users")
plt.xlabel("Total Registered Users")
plt.ylabel("State")

plt.show()

query17 = """
SELECT district,
       SUM(app_opens) AS total_app_opens
FROM map_user
GROUP BY district
ORDER BY total_app_opens DESC
LIMIT 10
"""

df17 = pd.read_sql(query17, connection)

print(df17)

plt.figure(figsize=(10,6))

plt.scatter(
    df17["district"],
    df17["total_app_opens"],
    s=df17["total_app_opens"]/5000,   # bubble size
    alpha=0.6
)

plt.xticks(rotation=45)

plt.title("Districts with Highest App Engagement")
plt.xlabel("District")
plt.ylabel("Total App Opens")

plt.show()

query18 = """
SELECT year,
       SUM(registered_users) AS total_users
FROM map_user
GROUP BY year
ORDER BY year
"""

df18 = pd.read_sql(query18, connection)

print(df18)

plt.figure(figsize=(10,6))

sns.barplot(
    x="year",
    y="total_users",
    data=df18
)

plt.title("PhonePe User Growth Over the Years")
plt.xlabel("Year")
plt.ylabel("Total Registered Users")

plt.show()

query19 = """
SELECT year,
       quarter,
       SUM(app_opens) AS total_app_opens
FROM map_user
GROUP BY year, quarter
ORDER BY year, quarter
"""

df19 = pd.read_sql(query19, connection)

print(df19)

pivot_df19 = df19.pivot(index="quarter", columns="year", values="total_app_opens")

print(pivot_df19)
pivot_df19.plot(
    kind="bar",
    stacked=True,
    figsize=(10,6)
)

plt.title("Quarterly App Engagement Trend")
plt.xlabel("Quarter")
plt.ylabel("Total App Opens")

plt.legend(title="Year")

plt.show()

query20 = """
SELECT state,
       SUM(app_opens) AS total_app_opens,
       SUM(registered_users) AS total_users,
       (SUM(app_opens) / SUM(registered_users)) AS engagement_ratio
FROM map_user
GROUP BY state
ORDER BY engagement_ratio DESC
"""

df20 = pd.read_sql(query20, connection)

print(df20)

plt.figure(figsize=(10,6))

plt.scatter(
    df20["total_users"],
    df20["total_app_opens"],
    alpha=0.6
)

plt.title("User Engagement by State")
plt.xlabel("Total Registered Users")
plt.ylabel("Total App Opens")

plt.show()

query21 = """
SELECT State,
       SUM(Transaction_amount) AS total_amount
FROM top_insurance
GROUP BY State
ORDER BY total_amount DESC
LIMIT 10
"""

df21 = pd.read_sql(query21, connection)

print(df21)

plt.figure(figsize=(10,6))

plt.hlines(
    y=df21["State"],
    xmin=0,
    xmax=df21["total_amount"]
)

plt.plot(
    df21["total_amount"],
    df21["State"],
    "o"
)

plt.title("Top States by Insurance Transaction Amount")
plt.xlabel("Total Insurance Transaction Amount")
plt.ylabel("State")

plt.show()

query22 = """
SELECT Pincode,
       SUM(Transaction_amount) AS total_amount
FROM top_insurance
GROUP BY Pincode
ORDER BY total_amount DESC
LIMIT 10
"""

df22 = pd.read_sql(query22, connection)

print(df22)

plt.figure(figsize=(10,6))

plt.scatter(
    df22["total_amount"],
    df22["Pincode"],
    s=120,
    alpha=0.7
)

plt.hlines(
    y=df22["Pincode"],
    xmin=0,
    xmax=df22["total_amount"],
    alpha=0.4
)

plt.title("Top Pin Codes by Insurance Transaction Amount")
plt.xlabel("Total Insurance Transaction Amount")
plt.ylabel("Pincode")

plt.show()

query23 = """
SELECT State,
       SUM(Transaction_count) AS total_transactions
FROM top_insurance
GROUP BY State
ORDER BY total_transactions DESC
LIMIT 10
"""

df23 = pd.read_sql(query23, connection)

print(df23)

plt.figure(figsize=(10,6))

sns.barplot(
    x="total_transactions",
    y="State",
    data=df23,
    palette="Blues_r"
)

plt.title("States with Highest Insurance Transaction Count")
plt.xlabel("Total Insurance Transactions")
plt.ylabel("State")

plt.show()

query24 = """
SELECT State,
       Pincode,
       Transaction_amount
FROM top_insurance
WHERE Year = 2022
AND Quarter = 1
ORDER BY Transaction_amount DESC
LIMIT 10
"""

df24 = pd.read_sql(query24, connection)

print(df24)

pivot_df24 = df24.pivot(
    index="State",
    columns="Pincode",
    values="Transaction_amount"
)

print(pivot_df24)
plt.figure(figsize=(10,6))

sns.heatmap(
    pivot_df24,
    annot=True,
    fmt=".0f",
    cmap="coolwarm"
)

plt.title("Insurance Transactions (2022 Q1)")
plt.xlabel("Pincode")
plt.ylabel("State")

plt.show()

query25 = """
SELECT Year,
       SUM(Transaction_amount) AS total_amount
FROM top_insurance
GROUP BY Year
ORDER BY Year
"""

df25 = pd.read_sql(query25, connection)

print(df25)

plt.figure(figsize=(10,6))

plt.step(
    df25["Year"],
    df25["total_amount"],
    where="mid",
    marker="o"
)

plt.title("Insurance Transaction Growth Over the Years")
plt.xlabel("Year")
plt.ylabel("Total Insurance Transaction Amount")

plt.grid(True)

plt.show()

phonepe_dashboard.py