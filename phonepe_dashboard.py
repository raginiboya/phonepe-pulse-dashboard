import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
import re

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="PhonePe Pulse Dashboard", layout="wide")

# ---------------- DATABASE CONNECTION ----------------
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="720767",
    database="phonepe"
)

def run_query(query):
    return pd.read_sql(query, connection)

# ---------------- STYLING ----------------
st.markdown("""
<style>
.stApp {
    background-color: #140a26;
    color: white;
}
section[data-testid="stSidebar"] {
    background-color: #1c1033;
}
.block-container {
    padding-top: 1rem;
}
div[data-testid="stMetric"] {
    background: #24103A;
    border: 1px solid #3f2a63;
    padding: 10px;
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- INDIA STATE COORDS ----------------
STATE_COORDS = {
    "andaman and nicobar islands": (11.7401, 92.6586),
    "andaman and nicobar": (11.7401, 92.6586),
    "andhra pradesh": (15.9129, 79.7400),
    "arunachal pradesh": (28.2180, 94.7278),
    "assam": (26.2006, 92.9376),
    "bihar": (25.0961, 85.3131),
    "chandigarh": (30.7333, 76.7794),
    "chhattisgarh": (21.2787, 81.8661),
    "dadra and nagar haveli and daman and diu": (20.1809, 73.0169),
    "dadra and nagar haveli": (20.1809, 73.0169),
    "daman and diu": (20.1809, 73.0169),
    "delhi": (28.6139, 77.2090),
    "nct of delhi": (28.6139, 77.2090),
    "goa": (15.2993, 74.1240),
    "gujarat": (22.2587, 71.1924),
    "haryana": (29.0588, 76.0858),
    "himachal pradesh": (31.1048, 77.1734),
    "jammu and kashmir": (33.7782, 76.5762),
    "jharkhand": (23.6102, 85.2799),
    "karnataka": (15.3173, 75.7139),
    "kerala": (10.8505, 76.2711),
    "ladakh": (34.1526, 77.5770),
    "lakshadweep": (10.5667, 72.6417),
    "madhya pradesh": (22.9734, 78.6569),
    "maharashtra": (19.7515, 75.7139),
    "manipur": (24.6637, 93.9063),
    "meghalaya": (25.4670, 91.3662),
    "mizoram": (23.1645, 92.9376),
    "nagaland": (26.1584, 94.5624),
    "odisha": (20.9517, 85.0985),
    "orissa": (20.9517, 85.0985),
    "puducherry": (11.9416, 79.8083),
    "pondicherry": (11.9416, 79.8083),
    "punjab": (31.1471, 75.3412),
    "rajasthan": (27.0238, 74.2179),
    "sikkim": (27.5330, 88.5122),
    "tamil nadu": (11.1271, 78.6569),
    "telangana": (18.1124, 79.0193),
    "tripura": (23.9408, 91.9882),
    "uttar pradesh": (26.8467, 80.9462),
    "uttarakhand": (30.0668, 79.0193),
    "west bengal": (22.9868, 87.8550),
}

def normalize_state(value):
    value = str(value).strip().lower()
    value = value.replace("&", "and")
    value = value.replace("-", " ")
    value = re.sub(r"\s+", " ", value)
    return value

def add_state_coords(df):
    df = df.copy()
    df["state_key"] = df["state"].apply(normalize_state)
    df["lat"] = df["state_key"].apply(lambda x: STATE_COORDS.get(x, (None, None))[0])
    df["lon"] = df["state_key"].apply(lambda x: STATE_COORDS.get(x, (None, None))[1])
    df = df.dropna(subset=["lat", "lon"])
    return df

def india_bubble_map(df, value_col, title):
    plot_df = add_state_coords(df)

    if plot_df.empty:
        st.warning("No states matched for map.")
        return None

    fig = px.scatter_geo(
        plot_df,
        lat="lat",
        lon="lon",
        size=value_col,
        color=value_col,
        hover_name="state",
        hover_data={value_col: ":,.0f"},
        projection="natural earth",
        title=title,
        color_continuous_scale="plasma",
        size_max=35
    )

    fig.update_geos(
        scope="asia",
        center={"lat": 22.5, "lon": 80},
        projection_scale=4.6,
        showland=True,
        landcolor="#22103A",
        showcountries=True,
        countrycolor="#6b5a87",
        showocean=True,
        oceancolor="#12071f",
        bgcolor="#140a26"
    )

    fig.update_layout(
        paper_bgcolor="#140a26",
        plot_bgcolor="#140a26",
        font=dict(color="white"),
        margin=dict(l=0, r=0, t=50, b=0),
        height=650,
        coloraxis_colorbar=dict(
            title=dict(text=value_col),
            tickfont=dict(color="white")
        )
    )

    return fig

def get_years(table_name):
    df = run_query(f"SELECT DISTINCT year FROM {table_name} ORDER BY year")
    return df["year"].tolist()

def get_quarters(table_name):
    df = run_query(f"SELECT DISTINCT quarter FROM {table_name} ORDER BY quarter")
    return df["quarter"].tolist()

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Page", ["Home", "Analysis"])

# ==================================================
# HOME PAGE
# ==================================================
if page == "Home":
    st.markdown("<h1 style='color:white;'>PHONEPE PULSE</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#b9a7d8;'>Interactive India Map Dashboard</p>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        category = st.selectbox("Category", ["Transactions", "Users", "Insurance"])

    if category == "Transactions":
        base_table = "aggregated_transaction"
    elif category == "Users":
        base_table = "map_user"
    else:
        base_table = "aggregated_insurance"

    years = get_years(base_table)
    quarters = get_quarters(base_table)

    with c2:
        year = st.selectbox("Year", years)

    with c3:
        quarter = st.selectbox("Quarter", quarters)

    with c4:
        view = st.selectbox("View", ["State", "Postal Code"])

    # TRANSACTIONS
    if category == "Transactions":
        if view == "State":
            df = run_query(f"""
                SELECT state, SUM(transaction_amount) AS total_amount
                FROM aggregated_transaction
                WHERE year={year} AND quarter={quarter}
                GROUP BY state
                ORDER BY total_amount DESC
            """)

            kpi = run_query(f"""
                SELECT SUM(transaction_amount) AS amount,
                       SUM(transaction_count) AS count
                FROM aggregated_transaction
                WHERE year={year} AND quarter={quarter}
            """)

            top_df = df.sort_values("total_amount", ascending=False).head(10)

            left, right = st.columns([2, 1])

            with left:
                m1, m2 = st.columns(2)
                with m1:
                    st.metric("Transaction Amount", f"₹ {int(kpi['amount'][0]):,}")
                with m2:
                    st.metric("Transactions", f"{int(kpi['count'][0]):,}")

                fig = india_bubble_map(df, "total_amount", f"Transactions by State - Q{quarter} {year}")
                if fig is not None:
                    st.plotly_chart(fig, width="stretch")

            with right:
                st.subheader("Top 10 States")
                st.dataframe(top_df, width="stretch")

        else:
            df = run_query(f"""
                SELECT pincode, SUM(transaction_amount) AS total_amount
                FROM top_transaction
                WHERE year={year} AND quarter={quarter}
                GROUP BY pincode
                ORDER BY total_amount DESC
                LIMIT 10
            """)
            st.subheader("Top 10 Postal Codes")
            st.dataframe(df, width="stretch")
            fig = px.bar(
                df,
                x="total_amount",
                y=df["pincode"].astype(str),
                orientation="h",
                color="total_amount"
            )
            st.plotly_chart(fig, width="stretch")

    # USERS
    elif category == "Users":
        if view == "State":
            df = run_query(f"""
                SELECT state, SUM(registered_users) AS total_users
                FROM map_user
                WHERE year={year} AND quarter={quarter}
                GROUP BY state
                ORDER BY total_users DESC
            """)

            kpi = run_query(f"""
                SELECT SUM(registered_users) AS users,
                       SUM(app_opens) AS opens
                FROM map_user
                WHERE year={year} AND quarter={quarter}
            """)

            top_df = df.sort_values("total_users", ascending=False).head(10)

            left, right = st.columns([2, 1])

            with left:
                m1, m2 = st.columns(2)
                with m1:
                    st.metric("Registered Users", f"{int(kpi['users'][0]):,}")
                with m2:
                    st.metric("App Opens", f"{int(kpi['opens'][0]):,}")

                fig = india_bubble_map(df, "total_users", f"Users by State - Q{quarter} {year}")
                if fig is not None:
                    st.plotly_chart(fig, width="stretch")

            with right:
                st.subheader("Top 10 States")
                st.dataframe(top_df, width="stretch")

        else:
            st.warning("Postal Code view is not available for Users in your current tables.")

    # INSURANCE
    elif category == "Insurance":
        if view == "State":
            df = run_query(f"""
                SELECT state, SUM(transaction_amount) AS total_amount
                FROM aggregated_insurance
                WHERE year={year} AND quarter={quarter}
                GROUP BY state
                ORDER BY total_amount DESC
            """)

            kpi = run_query(f"""
                SELECT SUM(transaction_amount) AS amount,
                       SUM(transaction_count) AS count
                FROM aggregated_insurance
                WHERE year={year} AND quarter={quarter}
            """)

            top_df = df.sort_values("total_amount", ascending=False).head(10)

            left, right = st.columns([2, 1])

            with left:
                m1, m2 = st.columns(2)
                with m1:
                    st.metric("Insurance Amount", f"₹ {int(kpi['amount'][0]):,}")
                with m2:
                    st.metric("Insurance Count", f"{int(kpi['count'][0]):,}")

                fig = india_bubble_map(df, "total_amount", f"Insurance by State - Q{quarter} {year}")
                if fig is not None:
                    st.plotly_chart(fig, width="stretch")

            with right:
                st.subheader("Top 10 States")
                st.dataframe(top_df, width="stretch")

        else:
            df = run_query(f"""
                SELECT pincode, SUM(transaction_amount) AS total_amount
                FROM top_insurance
                WHERE year={year} AND quarter={quarter}
                GROUP BY pincode
                ORDER BY total_amount DESC
                LIMIT 10
            """)
            st.subheader("Top 10 Postal Codes")
            st.dataframe(df, width="stretch")
            fig = px.bar(
                df,
                x="total_amount",
                y=df["pincode"].astype(str),
                orientation="h",
                color="total_amount"
            )
            st.plotly_chart(fig, width="stretch")

# ==================================================
# ANALYSIS PAGE
# ==================================================
elif page == "Analysis":
    st.title("Case Study Analysis")

    case_study = st.selectbox(
        "Select Case Study",
        [
            "Case Study 1 - Device Dominance and User Engagement Analysis",
            "Case Study 2 - Insurance Penetration and Growth Potential Analysis",
            "Case Study 3 - Transaction Analysis for Market Expansion",
            "Case Study 4 - User Engagement and Growth Strategy",
            "Case Study 5 - Insurance Transactions Analysis"
        ]
    )

    query_option = st.selectbox(
        "Select Query",
        ["Query 1", "Query 2", "Query 3", "Query 4", "Query 5"]
    )

    # CASE STUDY 1
    if case_study == "Case Study 1 - Device Dominance and User Engagement Analysis":
        if query_option == "Query 1":
            st.subheader("Top Device Brands by Registered Users")
            df = run_query("""
                SELECT brand, SUM(count) AS total_users
                FROM aggregated_user
                GROUP BY brand
                ORDER BY total_users DESC
                LIMIT 10
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="total_users", y="brand", orientation="h", color="total_users")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 2":
            st.subheader("Device Brand Market Share")
            df = run_query("""
                SELECT brand, AVG(percentage) AS avg_market_share
                FROM aggregated_user
                GROUP BY brand
                ORDER BY avg_market_share DESC
            """)
            st.dataframe(df, width="stretch")
            fig = px.pie(df, names="brand", values="avg_market_share", hole=0.4)
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 3":
            st.subheader("Device Usage Across States")
            df = run_query("""
                SELECT state, brand, SUM(count) AS total_users
                FROM aggregated_user
                GROUP BY state, brand
                ORDER BY state, total_users DESC
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df.head(50), x="state", y="total_users", color="brand", barmode="group")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 4":
            st.subheader("Device Usage Growth Over Time")
            df = run_query("""
                SELECT year, brand, SUM(count) AS total_users
                FROM aggregated_user
                GROUP BY year, brand
                ORDER BY year, total_users DESC
            """)
            st.dataframe(df, width="stretch")
            fig = px.line(df, x="year", y="total_users", color="brand", markers=True)
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 5":
            st.subheader("Quarterly Device Engagement Trend")
            df = run_query("""
                SELECT year, quarter, brand, SUM(count) AS total_users
                FROM aggregated_user
                GROUP BY year, quarter, brand
                ORDER BY year, quarter
            """)
            df["year_quarter"] = df["year"].astype(str) + "-Q" + df["quarter"].astype(str)
            st.dataframe(df, width="stretch")
            fig = px.line(df, x="year_quarter", y="total_users", color="brand", markers=True)
            st.plotly_chart(fig, width="stretch")

    # CASE STUDY 2
    elif case_study == "Case Study 2 - Insurance Penetration and Growth Potential Analysis":
        if query_option == "Query 1":
            st.subheader("Top States by Insurance Transaction Amount")
            df = run_query("""
                SELECT state, SUM(transaction_amount) AS total_insurance_amount
                FROM aggregated_insurance
                GROUP BY state
                ORDER BY total_insurance_amount DESC
                LIMIT 10
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="total_insurance_amount", y="state", orientation="h", color="total_insurance_amount")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 2":
            st.subheader("States with Highest Insurance Transaction Volume")
            df = run_query("""
                SELECT state, SUM(transaction_count) AS total_transactions
                FROM aggregated_insurance
                GROUP BY state
                ORDER BY total_transactions DESC
                LIMIT 10
            """)
            st.dataframe(df, width="stretch")
            fig = px.pie(df, names="state", values="total_transactions", hole=0.4)
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 3":
            st.subheader("Yearly Insurance Growth Trend")
            df = run_query("""
                SELECT year, SUM(transaction_amount) AS yearly_insurance_amount
                FROM aggregated_insurance
                GROUP BY year
                ORDER BY year
            """)
            st.dataframe(df, width="stretch")
            fig = px.line(df, x="year", y="yearly_insurance_amount", markers=True)
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 4":
            st.subheader("Quarterly Insurance Adoption")
            df = run_query("""
                SELECT year, quarter, SUM(transaction_count) AS quarterly_transactions
                FROM aggregated_insurance
                GROUP BY year, quarter
                ORDER BY year, quarter
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="quarter", y="quarterly_transactions", color="year", barmode="group")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 5":
            st.subheader("Insurance Adoption by State Over Time")
            df = run_query("""
                SELECT state, year, SUM(transaction_amount) AS total_amount
                FROM aggregated_insurance
                GROUP BY state, year
                ORDER BY state, year
            """)
            st.dataframe(df, width="stretch")
            fig = px.line(df, x="year", y="total_amount", color="state", markers=True)
            st.plotly_chart(fig, width="stretch")

    # CASE STUDY 3
    elif case_study == "Case Study 3 - Transaction Analysis for Market Expansion":
        if query_option == "Query 1":
            st.subheader("Top States by Total Transaction Amount")
            df = run_query("""
                SELECT state, SUM(transaction_amount) AS total_transaction_amount
                FROM aggregated_transaction
                GROUP BY state
                ORDER BY total_transaction_amount DESC
                LIMIT 10
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="total_transaction_amount", y="state", orientation="h", color="total_transaction_amount")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 2":
            st.subheader("States with Highest Transaction Volume")
            df = run_query("""
                SELECT state, SUM(transaction_count) AS total_transactions
                FROM aggregated_transaction
                GROUP BY state
                ORDER BY total_transactions DESC
                LIMIT 10
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="total_transactions", y="state", orientation="h", color="total_transactions")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 3":
            st.subheader("Yearly Transaction Growth")
            df = run_query("""
                SELECT year, SUM(transaction_amount) AS yearly_transaction_amount
                FROM aggregated_transaction
                GROUP BY year
                ORDER BY year
            """)
            st.dataframe(df, width="stretch")
            fig = px.line(df, x="year", y="yearly_transaction_amount", markers=True)
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 4":
            st.subheader("Transaction Trends by Quarter")
            df = run_query("""
                SELECT year, quarter, SUM(transaction_amount) AS quarterly_amount
                FROM aggregated_transaction
                GROUP BY year, quarter
                ORDER BY year, quarter
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="quarter", y="quarterly_amount", color="year", barmode="group")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 5":
            st.subheader("Most Popular Transaction Types")
            df = run_query("""
                SELECT transaction_type, SUM(transaction_count) AS total_transactions
                FROM aggregated_transaction
                GROUP BY transaction_type
                ORDER BY total_transactions DESC
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="total_transactions", y="transaction_type", orientation="h", color="total_transactions")
            st.plotly_chart(fig, width="stretch")

    # CASE STUDY 4
    elif case_study == "Case Study 4 - User Engagement and Growth Strategy":
        if query_option == "Query 1":
            st.subheader("Top States by Registered Users")
            df = run_query("""
                SELECT state, SUM(registered_users) AS total_users
                FROM map_user
                GROUP BY state
                ORDER BY total_users DESC
                LIMIT 10
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="total_users", y="state", orientation="h", color="total_users")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 2":
            st.subheader("Districts with Highest App Engagement")
            df = run_query("""
                SELECT district, SUM(app_opens) AS total_app_opens
                FROM map_user
                GROUP BY district
                ORDER BY total_app_opens DESC
                LIMIT 10
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="total_app_opens", y="district", orientation="h", color="total_app_opens")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 3":
            st.subheader("User Growth Over the Years")
            df = run_query("""
                SELECT year, SUM(registered_users) AS total_users
                FROM map_user
                GROUP BY year
                ORDER BY year
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="year", y="total_users", color="year")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 4":
            st.subheader("Quarterly App Engagement Trend")
            df = run_query("""
                SELECT year, quarter, SUM(app_opens) AS total_app_opens
                FROM map_user
                GROUP BY year, quarter
                ORDER BY year, quarter
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="quarter", y="total_app_opens", color="year", barmode="group")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 5":
            st.subheader("User Engagement Ratio by State")
            df = run_query("""
                SELECT state,
                       SUM(app_opens) AS total_app_opens,
                       SUM(registered_users) AS total_users,
                       (SUM(app_opens) / SUM(registered_users)) AS engagement_ratio
                FROM map_user
                GROUP BY state
                ORDER BY engagement_ratio DESC
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="engagement_ratio", y="state", orientation="h", color="engagement_ratio")
            st.plotly_chart(fig, width="stretch")

    # CASE STUDY 5
    elif case_study == "Case Study 5 - Insurance Transactions Analysis":
        if query_option == "Query 1":
            st.subheader("Top States by Insurance Transaction Amount")
            df = run_query("""
                SELECT state, SUM(transaction_amount) AS total_amount
                FROM top_insurance
                GROUP BY state
                ORDER BY total_amount DESC
                LIMIT 10
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="total_amount", y="state", orientation="h", color="total_amount")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 2":
            st.subheader("Top Pin Codes by Insurance Transaction Amount")
            df = run_query("""
                SELECT pincode, SUM(transaction_amount) AS total_amount
                FROM top_insurance
                GROUP BY pincode
                ORDER BY total_amount DESC
                LIMIT 10
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="total_amount", y=df["pincode"].astype(str), orientation="h", color="total_amount")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 3":
            st.subheader("States with Highest Insurance Transaction Count")
            df = run_query("""
                SELECT state, SUM(transaction_count) AS total_transactions
                FROM top_insurance
                GROUP BY state
                ORDER BY total_transactions DESC
                LIMIT 10
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="total_transactions", y="state", orientation="h", color="total_transactions")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 4":
            st.subheader("Insurance Transactions for a Specific Year and Quarter")
            df = run_query("""
                SELECT state, pincode, transaction_amount
                FROM top_insurance
                WHERE year = 2022 AND quarter = 1
                ORDER BY transaction_amount DESC
                LIMIT 10
            """)
            st.dataframe(df, width="stretch")
            fig = px.bar(df, x="transaction_amount", y=df["pincode"].astype(str), color="state")
            st.plotly_chart(fig, width="stretch")

        elif query_option == "Query 5":
            st.subheader("Insurance Transaction Growth Over the Years")
            df = run_query("""
                SELECT year, SUM(transaction_amount) AS total_amount
                FROM top_insurance
                GROUP BY year
                ORDER BY year
            """)
            st.dataframe(df, width="stretch")
            fig = px.line(df, x="year", y="total_amount", markers=True)
            st.plotly_chart(fig, width="stretch")