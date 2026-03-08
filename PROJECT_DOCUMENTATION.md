# PhonePe Pulse Data Visualization Dashboard

## Project Overview
This project analyzes digital payment trends across India using the PhonePe Pulse dataset. The objective is to convert raw transaction data into meaningful insights through interactive dashboards.

## Technologies Used
- Python
- Pandas
- MySQL
- Streamlit
- Plotly
- GitHub

## Data Source
The dataset used in this project comes from the official PhonePe Pulse GitHub repository.

https://github.com/PhonePe/pulse

## Data Processing
The project extracts JSON data from the dataset and converts it into structured tables stored in MySQL.

Tables used:
- aggregated_transaction
- aggregated_user
- map_user
- top_transaction
- top_insurance
- aggregated_insurance

## Dashboard Features
- Interactive India map
- State-wise transaction analysis
- User growth insights
- Insurance analysis
- Case study queries with charts

Case Study Analysis

To better understand digital payment behavior across India, several analytical case studies were performed using SQL queries and visualized through the Streamlit dashboard.

These case studies focus on identifying patterns in user adoption, transaction activity, and device usage.

Case Study 1: Top Device Brands by Users
Objective

The goal of this case study is to identify the most commonly used smartphone brands among PhonePe users.

Methodology

Data from the aggregated_user table was analyzed to calculate the total number of users associated with each smartphone brand.

SQL aggregation functions were used to sum the total user count for each brand.

Key Findings

The analysis shows that Xiaomi and Samsung dominate the smartphone market among PhonePe users.
Other brands such as Vivo, Oppo, and Realme also contribute significantly to the user base.

Insight

The dominance of affordable Android smartphones suggests that digital payment adoption is strongly driven by accessible mobile technology.

Visualization

The results are displayed in the dashboard using a tabular view and bar chart visualization.

Case Study 2: Top States by Transaction Amount
Objective

To identify which Indian states contribute the highest transaction values in the PhonePe ecosystem.

Methodology

Data from the top_transaction table was analyzed.
Transactions were aggregated by state and ordered in descending order to identify the top contributors.

Key Findings

States such as Maharashtra, Karnataka, and Uttar Pradesh consistently show the highest digital transaction values.

Insight

These states have higher digital payment adoption due to better infrastructure, larger population, and strong smartphone penetration.

Visualization

A Top 10 States table and an interactive map visualization were used to display the results.

Case Study 3: Transaction Growth Over Time
Objective

To analyze how digital payment transactions have grown across different years.

Methodology

Transaction values were aggregated by year using SQL SUM() functions.

Key Findings

The analysis reveals a significant growth trend in digital payments over the years, reflecting increasing trust and adoption of UPI-based systems.

Insight

Government initiatives promoting digital payments and the expansion of smartphone usage have contributed to this growth.

Visualization

A line chart visualization was used to represent transaction growth over time.

Case Study 4: Insurance Adoption Analysis
Objective

To evaluate how insurance services are being adopted through the PhonePe platform.

Methodology

Insurance transaction data was extracted from the aggregated_insurance and top_insurance tables.

Key Findings

Insurance transactions are gradually increasing, though they remain lower compared to regular payment transactions.

Insight

This indicates an opportunity for PhonePe to expand insurance awareness and promote financial protection services.

Visualization

The results were displayed using bar charts and comparative analysis tables.

## Key Insights
- Maharashtra and Karnataka show the highest transaction volumes.
- Xiaomi and Samsung dominate device usage.
- Digital payment adoption is rapidly increasing across India.

## Conclusion
This project demonstrates how data visualization techniques can transform raw financial data into actionable insights.