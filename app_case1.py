import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="720767",
    database="phonepe"
)

st.title("Case Study 1: Decoding Transaction Dynamics on PhonePe")

@st.cache_data(ttl=3600)
def run_query(sql):
    return pd.read_sql(sql, connection)

# Top 10 States by Transaction Amount
st.header("Top 10 States by Transaction Amount")
query_top_states = """
SELECT state, SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;
"""
df_top_states = run_query(query_top_states)
st.dataframe(df_top_states)

fig1, ax1 = plt.subplots(figsize=(10,6))
sns.barplot(x="total_amount", y="state", data=df_top_states, palette="viridis", ax=ax1)
ax1.set_title("Top 10 States by Transaction Amount")
ax1.set_xlabel("Transaction Amount")
ax1.set_ylabel("State")
st.pyplot(fig1)