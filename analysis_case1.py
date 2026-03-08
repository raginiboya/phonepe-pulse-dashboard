import matplotlib
matplotlib.use('TkAgg')  # ensures charts pop up on Windows

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

# -------------------------------
# 1️⃣ Connect to MySQL
# -------------------------------
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="720767",
    database="phonepe"
)

# -------------------------------
# 2️⃣ Query 1: Top 10 States by Transaction Amount (Bar + Pie)
# -------------------------------
query_top_states = """
SELECT state, SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;
"""
df_top_states = pd.read_sql(query_top_states, connection)
print("Top 10 States by Transaction Amount:\n", df_top_states)

# Bar Chart
plt.figure(figsize=(10,6))
sns.barplot(x="total_amount", y="state", data=df_top_states, palette="viridis")
plt.title("Top 10 States by Transaction Amount")
plt.xlabel("Transaction Amount")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# Pie Chart
plt.figure(figsize=(8,8))
plt.pie(
    df_top_states["total_amount"],
    labels=df_top_states["state"],
    autopct="%1.1f%%",
    startangle=140,
    colors=sns.color_palette("Set3")
)
plt.title("Transaction Share by Top 10 States")
plt.tight_layout()
plt.show()

# -------------------------------
# 3️⃣ Query 2: Quarterly Transaction Trend (Line Chart)
# -------------------------------
query_quarterly = """
SELECT year, quarter, SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY year, quarter
ORDER BY year, quarter;
"""
df_quarterly = pd.read_sql(query_quarterly, connection)
df_quarterly["Year_Quarter"] = df_quarterly["year"].astype(str) + "-Q" + df_quarterly["quarter"].astype(str)

plt.figure(figsize=(12,6))
plt.plot(df_quarterly["Year_Quarter"], df_quarterly["total_amount"], marker="o", color="blue")
plt.title("Quarterly Transaction Trend")
plt.xlabel("Year - Quarter")
plt.ylabel("Transaction Amount")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------
# 4️⃣ Query 3: Top 10 States by Transaction Count (Bar + Pie)
# -------------------------------
query_top_states_count = """
SELECT state, SUM(transaction_count) AS total_count
FROM aggregated_transaction
GROUP BY state
ORDER BY total_count DESC
LIMIT 10;
"""
df_top_states_count = pd.read_sql(query_top_states_count, connection)
print("Top 10 States by Transaction Count:\n", df_top_states_count)

# Bar Chart
plt.figure(figsize=(10,6))
sns.barplot(x="total_count", y="state", data=df_top_states_count, palette="magma")
plt.title("Top 10 States by Transaction Count")
plt.xlabel("Transaction Count")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# Pie Chart
plt.figure(figsize=(8,8))
plt.pie(
    df_top_states_count["total_count"],
    labels=df_top_states_count["state"],
    autopct="%1.1f%%",
    startangle=140,
    colors=sns.color_palette("Set2")
)
plt.title("Transaction Count Share by Top 10 States")
plt.tight_layout()
plt.show()

# -------------------------------
# 5️⃣ Query 4: Average Transaction Amount per Quarter (Line Chart)
# -------------------------------
query_avg_quarter = """
SELECT year, quarter, AVG(transaction_amount) AS avg_amount
FROM aggregated_transaction
GROUP BY year, quarter
ORDER BY year, quarter;
"""
df_avg_quarter = pd.read_sql(query_avg_quarter, connection)
df_avg_quarter["Year_Quarter"] = df_avg_quarter["year"].astype(str) + "-Q" + df_avg_quarter["quarter"].astype(str)

plt.figure(figsize=(12,6))
plt.plot(df_avg_quarter["Year_Quarter"], df_avg_quarter["avg_amount"], marker="o", color="green")
plt.title("Average Transaction Amount per Quarter")
plt.xlabel("Year - Quarter")
plt.ylabel("Average Transaction Amount")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------
# 6️⃣ Query 5: Total Transactions per State per Quarter (Multi-Line Chart)
# -------------------------------
query_state_quarter = """
SELECT state, year, quarter, SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state, year, quarter
ORDER BY state, year, quarter;
"""
df_state_quarter = pd.read_sql(query_state_quarter, connection)
df_state_quarter["Year_Quarter"] = df_state_quarter["year"].astype(str) + "-Q" + df_state_quarter["quarter"].astype(str)

plt.figure(figsize=(12,6))
for state in df_state_quarter["state"].unique():
    temp = df_state_quarter[df_state_quarter["state"] == state]
    plt.plot(temp["Year_Quarter"], temp["total_amount"], marker="o", label=state)

plt.title("Total Transactions per State per Quarter")
plt.xlabel("Year - Quarter")
plt.ylabel("Transaction Amount")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# -------------------------------
# Close MySQL Connection
# -------------------------------
connection.close()