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

## Case Study 1: Device Dominance and User Engagement Analysis

### Scenario
PhonePe aims to enhance user engagement and improve app performance by understanding user preferences across different device brands. The dataset contains information about registered users and app opens categorized by device brands, regions, and time periods. Understanding device dominance helps PhonePe optimize application performance and identify the most widely used devices.

---

### 1️⃣ Top Device Brands by Registered Users

#### SQL Query
SELECT brand,
       SUM(count) AS total_users
FROM aggregated_user
GROUP BY brand
ORDER BY total_users DESC
LIMIT 10;

#### Analysis Process
The analysis was performed using the **aggregated_user** table which stores user data grouped by device brand. The SQL query aggregates the number of registered users for each device brand using the **SUM(count)** function. The results are grouped by brand and sorted in descending order to identify the device brands with the highest number of PhonePe users.

#### Insights
The results indicate that certain smartphone brands dominate the PhonePe ecosystem. Popular Android brands such as **Xiaomi, Samsung, Vivo, and Oppo** typically contribute the largest share of users. This suggests that a significant portion of PhonePe users rely on affordable Android smartphones. Understanding these device preferences helps PhonePe prioritize app optimization for the most widely used devices and improve user experience.

#### Visualization
The results are displayed using a **Bar Chart** in the Streamlit dashboard. The bar chart compares different device brands based on the number of registered users, making it easy to identify the most dominant smartphone brands in the PhonePe user base.

---

### 2️⃣ Device Brand Market Share

#### SQL Query
SELECT brand,
       AVG(percentage) AS avg_market_share
FROM aggregated_user
GROUP BY brand
ORDER BY avg_market_share DESC;

#### Analysis Process
This analysis focuses on identifying the market share distribution of different smartphone brands used by PhonePe users. The **aggregated_user** table contains percentage data representing each brand's contribution to the total user base. The SQL query calculates the **average percentage share** of each device brand using the **AVG()** function. The results are grouped by brand and sorted in descending order to highlight brands with the highest market share.

#### Insights
The analysis reveals how the PhonePe user base is distributed across different smartphone brands. Brands such as **Xiaomi, Samsung, Vivo, and Oppo** typically occupy the largest share of the market. This indicates that Android-based smartphones dominate the digital payment ecosystem. Understanding market share distribution helps PhonePe identify dominant device platforms and prioritize performance optimization and partnerships with leading smartphone manufacturers.

#### Visualization
A **Pie Chart** is used to visualize the market share of different device brands. The pie chart effectively represents the percentage contribution of each brand, making it easy to understand how the PhonePe user base is distributed among smartphone manufacturers.

---

### 3️⃣ Device Usage Across States

#### SQL Query
SELECT state,
       brand,
       SUM(count) AS total_users
FROM aggregated_user
GROUP BY state, brand
ORDER BY state, total_users DESC;

#### Analysis Process
This analysis examines how different smartphone brands are used across various states in India. The data from the **aggregated_user** table is grouped by both **state** and **brand** to calculate the total number of users for each brand within each state. The **SUM(count)** function aggregates the number of users for each brand-state combination. The results are then ordered by state and user count to identify which device brands dominate in different regions.

#### Insights
The results highlight the regional distribution of smartphone brands used by PhonePe users. Certain brands tend to dominate specific states due to factors such as pricing, brand popularity, and regional market penetration. For example, affordable Android brands often have a stronger presence in many states, indicating their significant role in driving digital payment adoption. This insight helps PhonePe understand regional device preferences and optimize app performance accordingly.

#### Visualization
A **Stacked Bar Chart** is used to represent the distribution of device brands across different states. This visualization allows easy comparison of how various smartphone brands contribute to the PhonePe user base within each state.

---

### 4️⃣ Device Usage Growth Over Time

#### SQL Query
SELECT year,
       brand,
       SUM(count) AS total_users
FROM aggregated_user
GROUP BY year, brand
ORDER BY year, total_users DESC;

#### Analysis Process
This analysis focuses on understanding how smartphone device usage among PhonePe users has evolved over time. The **aggregated_user** table is used to group data by both **year** and **device brand**. The **SUM(count)** function calculates the total number of users for each brand in each year. By organizing the results chronologically, the query helps track the growth trend of different smartphone brands over multiple years.

#### Insights
The analysis reveals trends in smartphone adoption among PhonePe users over time. Certain brands show consistent growth, indicating increasing popularity and wider market penetration. The results also highlight how the expansion of affordable smartphones has contributed to the growth of digital payments in India. Monitoring device usage trends helps PhonePe anticipate future technology requirements and optimize application compatibility for rapidly growing devices.

#### Visualization
A **Line Chart** is used to visualize the growth of device usage over the years. This visualization clearly shows the trend of different smartphone brands and how their user base has increased or changed over time.

---

### 5️⃣ Quarterly Device Engagement Trend

#### SQL Query
SELECT year,
       quarter,
       brand,
       SUM(count) AS total_users
FROM aggregated_user
GROUP BY year, quarter, brand
ORDER BY year, quarter;

#### Analysis Process
This analysis focuses on evaluating how device engagement changes across different quarters within each year. The data from the **aggregated_user** table is grouped by **year, quarter, and device brand**. The **SUM(count)** function calculates the total number of users for each device brand within each quarter. By organizing the results chronologically by year and quarter, the analysis helps track seasonal trends and fluctuations in device usage.

#### Insights
The analysis helps identify patterns in device engagement throughout different quarters of the year. Some device brands may experience higher engagement during certain periods due to seasonal smartphone sales, new device launches, or promotional campaigns. This insight helps PhonePe understand how device usage evolves over time and ensures the application performs efficiently across devices that experience high engagement.

#### Visualization
A **Line Chart** is used to visualize quarterly device engagement trends. This visualization shows how device popularity changes across different quarters and helps identify patterns in user engagement over time.

## Case Study 2: Insurance Penetration and Growth Potential Analysis

### Scenario
PhonePe has expanded its services into the insurance sector, allowing users to purchase and manage various insurance policies through the platform. With increasing adoption of digital financial services, it is important to analyze how insurance transactions are distributed across different states and how this segment is growing over time. Understanding these trends can help PhonePe identify high-growth regions and develop targeted marketing strategies to promote insurance services.

---

### 1️⃣ Top States by Insurance Transaction Amount

#### SQL Query
SELECT state,
       SUM(transaction_amount) AS total_insurance_amount
FROM aggregated_insurance
GROUP BY state
ORDER BY total_insurance_amount DESC
LIMIT 10;

#### Analysis Process
This analysis identifies the states generating the highest insurance transaction value. The **aggregated_insurance** table was used to sum the total insurance transaction amount for each state using the **SUM(transaction_amount)** function. The results were grouped by state and sorted in descending order to highlight the top-performing states.

#### Insights
The results reveal which states contribute the most to insurance revenue on the PhonePe platform. States with higher economic activity and strong digital payment adoption typically show higher insurance transaction values. These regions represent strong markets where insurance services are already well adopted.

#### Visualization
A **Bar Chart** is used to visualize the top states by insurance transaction amount. This chart makes it easy to compare insurance revenue generated across different states.

---

### 2️⃣ States with Highest Insurance Transaction Volume

#### SQL Query
SELECT state,
       SUM(transaction_count) AS total_transactions
FROM aggregated_insurance
GROUP BY state
ORDER BY total_transactions DESC
LIMIT 10;

#### Analysis Process
This query evaluates which states have the highest number of insurance policy transactions. The **transaction_count** column is aggregated using the **SUM()** function to determine the total number of insurance purchases in each state.

#### Insights
The analysis highlights regions where users are most actively purchasing insurance policies. States with high transaction counts indicate stronger awareness and adoption of insurance services. These states represent mature markets where digital insurance adoption is already established.

#### Visualization
A **Donut Chart** is used to visualize the distribution of insurance transactions across states. This chart helps illustrate the proportion of insurance purchases contributed by each state.

---

### 3️⃣ Yearly Insurance Growth Trend

#### SQL Query
SELECT year,
       SUM(transaction_amount) AS yearly_insurance_amount
FROM aggregated_insurance
GROUP BY year
ORDER BY year;

#### Analysis Process
This analysis examines how insurance transaction value has grown over the years. Data from the **aggregated_insurance** table was grouped by year, and the total transaction amount was calculated using **SUM(transaction_amount)**.

#### Insights
The results show the growth trajectory of digital insurance services on the PhonePe platform. A steady increase in transaction value indicates rising awareness and adoption of insurance products among users.

#### Visualization
An **Area Chart** is used to visualize yearly insurance growth trends. This visualization effectively highlights the increase in insurance transaction values over time.

---

### 4️⃣ Quarterly Insurance Adoption

#### SQL Query
SELECT year,
       quarter,
       SUM(transaction_count) AS quarterly_transactions
FROM aggregated_insurance
GROUP BY year, quarter
ORDER BY year, quarter;

#### Analysis Process
This analysis evaluates seasonal patterns in insurance adoption by grouping transactions by both **year** and **quarter**. The total number of insurance transactions is calculated using **SUM(transaction_count)**.

#### Insights
The results reveal seasonal variations in insurance purchases. Certain quarters may show higher transaction activity due to financial planning cycles, policy renewals, or promotional campaigns.

#### Visualization
A **Heatmap** is used to represent quarterly insurance adoption trends. The heatmap highlights periods with higher or lower insurance activity, making seasonal patterns easier to identify.

---

### 5️⃣ Insurance Adoption by State Over Time

#### SQL Query
SELECT state,
       year,
       SUM(transaction_amount) AS total_amount
FROM aggregated_insurance
GROUP BY state, year
ORDER BY state, year;

#### Analysis Process
This query analyzes how insurance transaction values have changed across different states over multiple years. The data is grouped by both **state** and **year**, allowing the analysis of regional growth patterns.

#### Insights
The results highlight states where insurance adoption is steadily increasing over time. These states represent strong growth opportunities where PhonePe can expand its insurance offerings and partnerships.

#### Visualization
A **Line Chart** is used to visualize insurance adoption trends for different states over time. This chart helps track growth patterns and compare adoption levels across regions.

## Case Study 3: Transaction Analysis for Market Expansion

### Scenario
PhonePe operates in a highly competitive digital payments market. Understanding transaction patterns across states and over time is important for identifying growth opportunities and planning expansion strategies. By analyzing transaction amount, transaction volume, and transaction types, PhonePe can determine which regions and services contribute most to its platform usage.

---

### 1️⃣ Top States by Total Transaction Amount

#### SQL Query
SELECT state,
       SUM(transaction_amount) AS total_transaction_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_transaction_amount DESC
LIMIT 10;

#### Analysis Process
This analysis identifies the states that generate the highest digital transaction value on the PhonePe platform. The **aggregated_transaction** table is used to calculate the total transaction amount for each state using the **SUM(transaction_amount)** function. The results are grouped by state and sorted in descending order to determine the top-performing states.

#### Insights
The analysis highlights states that contribute the most to the overall transaction value. States with higher digital adoption and larger populations tend to generate greater transaction amounts. These regions represent strong markets where PhonePe services are widely used and have high financial activity.

#### Visualization
A **Bar Chart** is used to compare the top states by transaction amount. The chart provides a clear comparison of transaction value across different states.

---

### 2️⃣ States with Highest Transaction Volume

#### SQL Query
SELECT state,
       SUM(transaction_count) AS total_transactions
FROM aggregated_transaction
GROUP BY state
ORDER BY total_transactions DESC
LIMIT 10;

#### Analysis Process
This query analyzes the number of transactions occurring in each state. Using the **SUM(transaction_count)** function, the total transaction volume is calculated for each state. The results are grouped by state and ranked in descending order to determine which states have the highest number of digital transactions.

#### Insights
The results reveal the states where PhonePe is most actively used for daily transactions. High transaction counts indicate strong digital payment adoption and frequent usage of the platform. These regions represent key markets where PhonePe has strong user engagement.

#### Visualization
A **Treemap** is used to visualize transaction volume distribution across states. The treemap helps illustrate which states contribute the most to the total number of transactions.

---

### 3️⃣ Yearly Transaction Growth

#### SQL Query
SELECT year,
       SUM(transaction_amount) AS yearly_transaction_amount
FROM aggregated_transaction
GROUP BY year
ORDER BY year;

#### Analysis Process
This analysis evaluates how digital transaction value has grown over time. The **aggregated_transaction** table is grouped by year, and the total transaction amount is calculated using **SUM(transaction_amount)**. The results are ordered chronologically to track year-by-year growth.

#### Insights
The results show a consistent increase in digital transactions over the years. This growth reflects the increasing adoption of digital payment systems and the expanding reach of platforms like PhonePe.

#### Visualization
A **Line Chart** is used to represent yearly transaction growth. This chart clearly highlights the upward trend in transaction values over time.

---

### 4️⃣ Transaction Trends by Quarter

#### SQL Query
SELECT year,
       quarter,
       SUM(transaction_amount) AS quarterly_amount
FROM aggregated_transaction
GROUP BY year, quarter
ORDER BY year, quarter;

#### Analysis Process
This analysis explores how transaction values change across different quarters within each year. The data is grouped by **year and quarter**, and the total transaction amount is calculated using **SUM(transaction_amount)**.

#### Insights
The analysis helps identify seasonal patterns in digital payment usage. Certain quarters may experience higher transaction activity due to festive seasons, promotional campaigns, or increased consumer spending.

#### Visualization
A **Multi-Line Chart** is used to visualize transaction trends across quarters. This visualization helps track seasonal variations and compare quarterly performance across years.

---

### 5️⃣ Most Popular Transaction Types

#### SQL Query
SELECT transaction_type,
       SUM(transaction_count) AS total_transactions
FROM aggregated_transaction
GROUP BY transaction_type
ORDER BY total_transactions DESC;

#### Analysis Process
This query analyzes the popularity of different transaction types on the PhonePe platform. The **transaction_count** column is aggregated using **SUM()** to determine how frequently each transaction type occurs.

#### Insights
The analysis reveals which payment categories are most commonly used by PhonePe users. Popular transaction types such as peer-to-peer transfers, merchant payments, and bill payments indicate the primary ways users interact with the platform.

#### Visualization
A **Bar Chart** is used to display the distribution of transaction types. This visualization helps identify which transaction categories contribute most to platform usage.

## Case Study 4: User Engagement and Growth Strategy

### Scenario
PhonePe aims to strengthen its market presence by analyzing user engagement patterns across different states and districts. By examining the number of registered users and app opens, the company can better understand user behavior, engagement levels, and potential growth opportunities. This analysis helps identify regions where user adoption is high and where further engagement strategies can be implemented.

---

### 1️⃣ Top States by Registered Users

#### SQL Query
SELECT state,
       SUM(registered_users) AS total_users
FROM map_user
GROUP BY state
ORDER BY total_users DESC
LIMIT 10;

#### Analysis Process
This analysis identifies the states with the highest number of PhonePe users. The **map_user** table is used to aggregate the total number of registered users in each state using the **SUM(registered_users)** function. The results are grouped by state and sorted in descending order to highlight the states with the largest user base.

#### Insights
States with the highest number of registered users represent regions where PhonePe has successfully achieved strong adoption. These areas indicate high digital payment awareness and smartphone penetration. Identifying these states helps PhonePe understand where the platform is most widely used.

#### Visualization
A **Bar Chart** is used to display the top states by registered users. The chart allows easy comparison of user distribution across different states.

---

### 2️⃣ Districts with Highest App Engagement

#### SQL Query
SELECT district,
       SUM(app_opens) AS total_app_opens
FROM map_user
GROUP BY district
ORDER BY total_app_opens DESC
LIMIT 10;

#### Analysis Process
This analysis focuses on identifying districts where PhonePe users interact with the application most frequently. The **SUM(app_opens)** function calculates the total number of app openings for each district. The results are grouped by district and ranked in descending order.

#### Insights
Districts with the highest number of app opens indicate regions with strong user engagement and frequent usage of the PhonePe platform. These areas demonstrate higher reliance on digital payment services.

#### Visualization
A **Bubble Chart** is used to represent app engagement across districts. The bubble size represents the level of app engagement, allowing easy identification of high-activity regions.

---

### 3️⃣ User Growth Over the Years

#### SQL Query
SELECT year,
       SUM(registered_users) AS total_users
FROM map_user
GROUP BY year
ORDER BY year;

#### Analysis Process
This analysis evaluates how PhonePe's user base has grown over time. The **map_user** table is grouped by year, and the **SUM(registered_users)** function calculates the total number of users for each year.

#### Insights
The results highlight a steady increase in the number of registered users over time, reflecting the rapid adoption of digital payment platforms in India. This growth indicates increasing trust in digital financial services.

#### Visualization
A **Column Chart** is used to represent yearly user growth. The visualization helps illustrate how the PhonePe user base has expanded over time.

---

### 4️⃣ Quarterly App Engagement Trend

#### SQL Query
SELECT year,
       quarter,
       SUM(app_opens) AS total_app_opens
FROM map_user
GROUP BY year, quarter
ORDER BY year, quarter;

#### Analysis Process
This query analyzes how app engagement changes across different quarters. The data is grouped by both **year and quarter**, and the **SUM(app_opens)** function calculates the total number of app opens in each period.

#### Insights
The analysis reveals seasonal patterns in user engagement. Certain quarters may experience higher activity due to festivals, promotions, or increased online transactions.

#### Visualization
A **Stacked Column Chart** is used to visualize quarterly engagement trends, allowing comparison of engagement levels across different periods.

---

### 5️⃣ User Engagement Ratio by State

#### SQL Query
SELECT state,
       SUM(app_opens) AS total_app_opens,
       SUM(registered_users) AS total_users,
       (SUM(app_opens) / SUM(registered_users)) AS engagement_ratio
FROM map_user
GROUP BY state
ORDER BY engagement_ratio DESC;

#### Analysis Process
This analysis compares app engagement with the number of registered users to determine how actively users interact with the platform. The engagement ratio is calculated by dividing total app opens by total registered users for each state.

#### Insights
States with higher engagement ratios indicate that users frequently interact with the PhonePe app. These regions represent strong user loyalty and consistent usage patterns.

#### Visualization
A **Scatter Plot** is used to visualize engagement ratios across states, helping identify areas with high or low user interaction.

---

## Case Study 5: Insurance Transactions Analysis

### Scenario
PhonePe analyzes insurance transaction data to identify regions with the highest activity in the insurance segment. By examining state-level, district-level, and pin code-level transaction data, the company can identify high-performing regions and understand how insurance adoption varies geographically.

---

### 1️⃣ Top States by Insurance Transaction Amount

#### SQL Query
SELECT State,
       SUM(Transaction_amount) AS total_amount
FROM top_insurance
GROUP BY State
ORDER BY total_amount DESC
LIMIT 10;

#### Analysis Process
This query calculates the total insurance transaction value generated in each state. The **SUM(Transaction_amount)** function aggregates the total transaction amount, and the results are grouped by state to identify the top-performing regions.

#### Insights
States with the highest transaction amounts represent regions where insurance services are widely adopted. These areas may have higher financial awareness and stronger digital service penetration.

#### Visualization
A **Lollipop Chart** is used to display the states generating the highest insurance transaction values.

---

### 2️⃣ Top Pin Codes by Insurance Transaction Amount

#### SQL Query
SELECT Pincode,
       SUM(Transaction_amount) AS total_amount
FROM top_insurance
GROUP BY Pincode
ORDER BY total_amount DESC
LIMIT 10;

#### Analysis Process
This analysis identifies specific pin code regions that generate the highest insurance transaction values. The **SUM(Transaction_amount)** function aggregates total insurance spending within each pin code.

#### Insights
Pin codes with high transaction values highlight localized areas where insurance adoption is particularly strong. These areas may represent important target markets for insurance providers.

#### Visualization
A **Dot Plot** is used to visualize the top pin codes by insurance transaction amount.

---

### 3️⃣ States with Highest Insurance Transaction Count

#### SQL Query
SELECT State,
       SUM(Transaction_count) AS total_transactions
FROM top_insurance
GROUP BY State
ORDER BY total_transactions DESC
LIMIT 10;

#### Analysis Process
This query identifies the states where the largest number of insurance transactions occur. The **SUM(Transaction_count)** function aggregates the number of insurance purchases in each state.

#### Insights
States with the highest transaction counts indicate strong insurance adoption and frequent usage of digital insurance services.

#### Visualization
A **Funnel-Style Chart** is used to represent the states with the highest number of insurance transactions.

---

### 4️⃣ Insurance Transactions for a Specific Year and Quarter

#### SQL Query
SELECT State,
       Pincode,
       Transaction_amount
FROM top_insurance
WHERE Year = 2022
AND Quarter = 1
ORDER BY Transaction_amount DESC
LIMIT 10;

#### Analysis Process
This analysis focuses on insurance transactions within a specific time period. Filtering the data by year and quarter helps identify regions that generated the highest insurance transaction value during that period.

#### Insights
The results highlight the most active states and pin codes during the selected quarter, providing insights into regional performance during that timeframe.

#### Visualization
A **Bar Chart** is used to display the top regions generating insurance transaction values for the selected quarter.

---

### 5️⃣ Insurance Transaction Growth Over the Years

#### SQL Query
SELECT Year,
       SUM(Transaction_amount) AS total_amount
FROM top_insurance
GROUP BY Year
ORDER BY Year;

#### Analysis Process
This analysis examines how insurance transaction values have grown over time. The data is grouped by year, and total transaction amounts are calculated using **SUM(Transaction_amount)**.

#### Insights
The results reveal the overall growth trend of digital insurance services on the PhonePe platform. Increasing values indicate growing awareness and adoption of insurance services among users.

#### Visualization
A **Line Chart** is used to illustrate the growth of insurance transaction values across years.

## Key Insights
- Maharashtra and Karnataka show the highest transaction volumes.
- Xiaomi and Samsung dominate device usage.
- Digital payment adoption is rapidly increasing across India.

## Conclusion
This project demonstrates how data visualization techniques can transform raw financial data into actionable insights.