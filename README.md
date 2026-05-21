# ☁️ End-to-End Cloud E-Commerce Analytics Pipeline

> Production-style cloud analytics solution built with Python, Google Cloud Platform (GCP), BigQuery, SQL, and Power BI for automated E-Commerce reporting and customer intelligence.

![Python](https://img.shields.io/badge/Python-ETL-blue)
![BigQuery](https://img.shields.io/badge/Google_BigQuery-Data_Warehouse-orange)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![Google Cloud](https://img.shields.io/badge/GCP-Cloud_Analytics-green)
![SQL](https://img.shields.io/badge/SQL-Analytics-red)

---

# 📌 Project Overview

This project transforms **100k+ Brazilian E-Commerce records** from the Olist marketplace into actionable business intelligence through a fully automated cloud analytics pipeline.

The solution combines:

- Cloud Storage
- ETL Automation
- Data Warehousing
- SQL Transformations
- Advanced Analytics
- Interactive Power BI Dashboards

to simulate a real-world analytics engineering workflow used in modern data teams.

---

# 🎯 Project Type

**Portfolio Project | Cloud Analytics Engineering | Business Intelligence | Data Warehousing**

---

# 📊 Dataset Scale

- 100,000+ Orders Processed
- 300,000+ Order Items Analyzed
- 9 Relational Datasets Integrated
- Multi-layer Cloud Data Architecture
- Automated ETL Pipeline
- Executive & Operational Reporting

---

# 🚀 Business Objectives

This project was designed to solve key business problems across:

- Executive Sales Monitoring
- Customer Segmentation
- Logistics & Delivery Performance
- Operational Efficiency

### Key Goals

- Identify high-value and at-risk customers
- Monitor delivery delays and operational bottlenecks
- Build scalable cloud-based reporting architecture
- Automate ingestion and transformation workflows
- Deliver executive-level business intelligence dashboards

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

---

# 📂 Datasets Processed

The pipeline integrates 9 relational datasets including:

- Customers
- Orders
- Payments
- Reviews
- Products
- Sellers
- Geolocation
- Order Items
- Product Translation

---

# 🛠️ Tech Stack

## Cloud & Data Engineering

- Google Cloud Storage (GCS)
- Google BigQuery
- Python
- Pandas
- SQL

## Business Intelligence

- Power BI
- DAX
- Star Schema Modeling

## Analytics

- RFM Customer Segmentation
- KPI Engineering
- Delivery Performance Analysis
- Revenue Trend Analysis
- Operational Analytics

## Development Environment

- Jupyter Notebook
- VS Code
- Git & GitHub

---

# 📊 Power BI Dashboards

## 1️⃣ Executive Sales Dashboard

Provides executive-level visibility into revenue performance, delivery operations, and customer behavior.

### Key Metrics

- Total Revenue
- Total Orders
- Average Order Value
- Delivery Performance
- Revenue Trends
- Customer Segment Contribution

### Business Insights

- Identified seasonal sales patterns
- Tracked delayed order impact
- Monitored state-level revenue performance
- Analyzed customer segment contributions

![Executive Sales Dashboard](dashboards/executive_sales_dashboard.png)

---

## 2️⃣ Customer Segmentation Dashboard

Built using RFM (Recency, Frequency, Monetary) modeling to classify customer behavior and identify retention opportunities.

### Customer Segments

- Champions
- Loyal Customers
- Potential Loyalists
- At Risk Customers

### Business Impact

- Identified high-value customer clusters
- Highlighted churn-risk customers
- Supported retention strategy development
- Improved customer intelligence reporting

![Customer Segmentation Dashboard](dashboards/customer_segmentation_dashboard.png)

---

## 3️⃣ Delivery & Operations Dashboard

Focused on logistics monitoring and operational performance analysis across regions and delivery timelines.

### Operational KPIs

- Delivered Orders
- Delayed Orders
- Average Delivery Days
- State-Level Delivery Performance
- Delivery Distribution Analysis

### Operational Insights

- Identified delivery bottlenecks
- Measured delayed order impact
- Monitored fulfillment efficiency
- Analyzed regional delivery performance

![Delivery Operations Dashboard](dashboards/delivery_operations_dashboard.png)

---

# 📈 Advanced Analytics

## RFM Customer Segmentation

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
├── scripts/
│   └── etl/
│
├── dashboards/
│   ├── executive_sales_dashboard.png
│   ├── customer_segmentation_dashboard.png
│   └── delivery_operations_dashboard.png
│
├── docs/
│
├── sql/
│
├── notebooks/
│
├── .gitignore
│
├── requirements.txt
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

# ⚡ Project Setup

## Clone Repository

```bash
git clone https://github.com/yourusername/olist-cloud-etl-pipeline.git
cd olist-cloud-etl-pipeline
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Google Cloud

- Create a GCP Project
- Enable BigQuery API
- Enable Cloud Storage API
- Configure Service Account Credentials

## Run ETL Pipeline

```bash
python scripts/etl/upload_to_gcs.py
python scripts/etl/load_to_bigquery.py
```

---

# 📦 Requirements

```txt
pandas
google-cloud-storage
google-cloud-bigquery
pandas-gbq
numpy
jupyter
```

---

# ⭐ Business Value Delivered

This project demonstrates how modern analytics teams build scalable cloud reporting systems capable of transforming raw transactional data into executive-level business intelligence.

The solution enables:

- Automated cloud-based reporting
- Scalable analytics infrastructure
- Customer retention analysis
- Operational performance monitoring
- Executive KPI tracking
- Interactive business intelligence dashboards

---

# 📌 Key Skills Demonstrated

- Cloud Data Engineering
- ETL Pipeline Development
- Data Warehousing
- SQL Analytics
- Power BI Dashboarding
- KPI Development
- Business Intelligence
- RFM Customer Analytics
- Git Version Control
- Cloud Architecture Design

---

# 🔮 Future Enhancements

- ETL orchestration using Apache Airflow
- Real-time dashboard refresh
- CI/CD integration using GitHub Actions
- Predictive churn modeling with Scikit-learn
- Cloud deployment optimization

---

# 👨‍💻 Author

## Babi Clovis Abah

- Data Analytics & Cloud Analytics Portfolio Project
- Power BI Developer | SQL Analyst | Cloud Analytics Enthusiast

### Connect With Me

- LinkedIn: https://www.linkedin.com/in/babi-abah-061555406/
- GitHub: https://github.com/babiabah6-cell
