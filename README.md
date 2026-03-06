# Retail Data Engineering Pipeline with Analytics Dashboard

## Project Overview

This project demonstrates an **end-to-end Retail Data Engineering Pipeline** built using Python.
The system processes retail transaction data, performs data cleaning and feature engineering, trains machine learning models, and provides an **interactive analytics dashboard** for business insights.

The dashboard allows users to explore sales performance, product trends, and customer insights using interactive visualizations.

Dataset contains **500k+ retail transactions**.

---

## Project Architecture

```
Retail Dataset (CSV)
        ↓
Data Ingestion
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Database Storage
        ↓
Data Analysis
        ↓
Machine Learning Models
        ↓
Streamlit Analytics Dashboard
```

---

## Project Structure

```
retail-data-engineering-pipeline
│
├── data
│   └── transformed_retail.csv
│
├── scripts
│   ├── ingest_data.py
│   ├── clean_data.py
│   ├── feature_engineering.py
│   ├── database_load.py
│   ├── data_analysis.py
│   ├── data_visualization.py
│   ├── ml_models.py
│   └── pipeline.py
│
├── dashboard.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Data Engineering Pipeline

The project includes the following pipeline stages:

### 1. Data Ingestion

Load raw retail dataset from CSV.

### 2. Data Cleaning

* Handle missing values
* Remove invalid transactions
* Data formatting

### 3. Feature Engineering

* Create **TotalAmount**
* Extract **Month** from invoice date
* Generate useful analytical features

### 4. Database Storage

Processed data can be stored in a database for scalable analytics.

### 5. Data Analysis

Explore key business insights such as:

* monthly sales
* top countries
* product demand
* customer activity

### 6. Machine Learning Models

The following models are trained to analyze sales patterns:

* Linear Regression
* Decision Tree
* Random Forest
* Support Vector Machine
* Naive Bayes (sales category classification)

---

## Analytics Dashboard

The project includes an **interactive dashboard built using Streamlit and Plotly**.

### Dashboard Features

* KPI metrics for business performance
* Country filter
* Month filter
* Monthly sales trend visualization
* Top selling products analysis
* Country-wise sales analysis
* Sales distribution insights
* Interactive charts with zoom and hover

All charts update **in real-time based on filter selections**.

---

## Dashboard Preview


![Retail Dashboard](dashboard.png)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Srikarsaitej/retail-data-engineering-pipeline.git
```

Move into project folder:

```bash
cd retail-data-engineering-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Data Pipeline

Execute the complete pipeline:

```bash
python scripts/pipeline.py
```

---

## Run the Dashboard

Start the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

Open browser:

```
http://localhost:8501
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* Plotly
* Git
* GitHub

---

## Key Highlights

* End-to-end **Data Engineering Pipeline**
* Machine learning models for retail analytics
* Interactive **business dashboard**
* Real-time filtering and insights
* Scalable project structure

---

## Author

**Srikar Sai Tej**

GitHub:
https://github.com/Srikarsaitej

---
