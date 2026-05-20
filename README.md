# ☁️ End-to-End Cloud E-Commerce Analytics Pipeline

> Building a production-style cloud analytics solution using Python, Google Cloud Storage, BigQuery, SQL, and Power BI to automate E-Commerce data ingestion, transformation, warehousing, and business intelligence reporting.

---

# 📌 Project Overview

This project transforms 100k+ Brazilian E-Commerce records from the Olist marketplace into actionable business intelligence through a fully automated cloud analytics pipeline.

The solution combines:

* Cloud Storage
* ETL Automation
* Data Warehousing
* SQL Transformations
* Advanced Analytics
* Interactive Power BI Dashboards

to simulate a real-world analytics engineering workflow used in modern data teams.

---

# 🚀 Business Objectives

This project was designed to solve key business problems across:

* Executive Sales Monitoring
* Customer Segmentation
* Logistics & Delivery Performance
* Operational Efficiency

Key goals included:

* Identifying high-value and at-risk customers
* Monitoring delivery delays and operational bottlenecks
* Building scalable cloud-based reporting architecture
* Automating ingestion and transformation workflows

---

# 🏗️ Cloud Architecture

```text
Local CSV Files
        ↓
Python ETL Pipeline
        ↓
Google Cloud Storage (Raw Layer)
        ↓
BigQuery Data Warehouse
        ↓
SQL Transformations
        ↓
Power BI Dashboards
```

---

# ⚙️ Automated ETL Pipeline

Developed Python-based ETL workflows to automate:

✅ Bulk upload of raw CSV datasets to Google Cloud Storage

✅ Automated ingestion from GCS into BigQuery

✅ Data cleaning and transformation using SQL and Python

✅ Analytics-ready table generation for Power BI reporting

The pipeline processes 9 relational datasets including:

* Customers
* Orders
* Payments
* Reviews
* Products
* Sellers
* Geolocation
* Order Items
* Product Translation

---

# 🛠️ Tech Stack

## Cloud & Data Engineering

* Google Cloud Storage (GCS)
* Google BigQuery
* Python
* Pandas
* SQL

## Business Intelligence

* Power BI
* DAX
* Star Schema Modeling

## Analytics

* RFM Customer Segmentation
* KPI Engineering
* Delivery Performance Analysis
* Revenue Trend Analysis
* Operational Analytics

## Development Environment

* Jupyter Notebook
* VS Code
* Git & GitHub

---

# 📊 Power BI Dashboards

## 1️⃣ Executive Sales Dashboard

Provides high-level business monitoring including:

* Total Revenue
* Total Orders
* Average Order Value
* Delivery KPIs
* Revenue Trends
* State-Level Performance

### Key Insights

* Identified seasonal revenue peaks
* Monitored delayed order trends
* Tracked operational performance across states

---

## 2️⃣ Customer Segmentation Dashboard

Built an advanced RFM segmentation model to classify customers based on:

* Recency
* Frequency
* Monetary Value

### Customer Segments

* Champions
* Loyal Customers
* Potential Loyalists
* At Risk Customers

### Business Impact

* Identified high-value customer clusters
* Highlighted customers likely to churn
* Supported targeted retention strategies

---

## 3️⃣ Delivery Operations Dashboard

Focused on operational and logistics intelligence including:

* Delivery Trends
* Average Delivery Time
* Delay Monitoring
* Delivery Distribution
* State-Level Delivery Performance

### Operational Insights

* Identified delivery bottlenecks
* Measured delayed order impact
* Monitored fulfillment efficiency

---

# 📈 Advanced Analytics

## RFM Modeling

Implemented customer segmentation using Python:

```python
snapshot_date = df_full['order_purchase_timestamp'].max() + pd.Timedelta(days=1)

rfm = df_full.groupby('customer_unique_id').agg({
    'order_purchase_timestamp': lambda x: (snapshot_date - x.max()).days,
    'order_id': 'nunique',
    'payment_value': 'sum'
}).rename(columns={
    'order_purchase_timestamp': 'Recency',
    'order_id': 'Frequency',
    'payment_value': 'Monetary'
})
```

---

# 📂 Project Structure

```text
olist-cloud-etl-pipeline/
│
├── data/
│   └── raw/
│
├── Script/
│   └── etl/
│
├── dashboards/
│
├── docs/
│
├── sql/
│
├── .gitignore
│
└── README.md
```

---

# 🔄 End-to-End Workflow

## Step 1 — Raw Data Collection

Downloaded raw E-Commerce CSV datasets from the Olist dataset.

## Step 2 — Cloud Storage Ingestion

Uploaded datasets into Google Cloud Storage using automated Python scripts.

## Step 3 — BigQuery Warehousing

Loaded raw files into BigQuery tables for scalable cloud querying.

## Step 4 — Data Transformation

Performed SQL and Python transformations to generate analytics-ready tables.

## Step 5 — Power BI Reporting

Connected Power BI to BigQuery for interactive dashboard development.

---

# 📌 Key Skills Demonstrated

* Cloud Data Engineering
* ETL Pipeline Development
* Data Warehousing
* SQL Analytics
* Power BI Dashboarding
* KPI Development
* Business Intelligence
* RFM Customer Analytics
* Git Version Control
* Cloud Architecture Design

---

# 📷 Dashboard Previews

> Add screenshots inside the `/dashboards` folder and link them here.

Example:

```markdown
![Executive Dashboard](dashboards/executive_dashboard.png)
```

---

# 🔮 Future Enhancements

* ETL orchestration using Apache Airflow
* Real-time dashboard refresh
* CI/CD integration using GitHub Actions
* Predictive churn modeling with Scikit-learn
* Cloud deployment optimization

---

# 👨‍💻 Author

## Babi Clovis Abah

Aspiring Cloud Data Analyst & Analytics Engineer focused on:

* Data Engineering
* Business Intelligence
* Cloud Analytics
* ETL Automation

---

# 🤝 Connect With Me



*  LinkedIn: https://www.linkedin.com/in/babi-abah-061555406/
* GitHub: https://github.com/babiabah6-cell


---

⭐ If you found this project valuable, feel free to star the repository.
