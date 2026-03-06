
RETAIL DATA ENGINEERING & MACHINE LEARNING PIPELINE

## Project Overview

This project demonstrates a complete **Retail Data Engineering Pipeline** built using Python.
The pipeline performs **data ingestion, cleaning, feature engineering, database storage, analysis, visualization, and machine learning modeling**.

The goal of this project is to simulate an **industry-level data pipeline used in retail analytics systems**.

---

# Project Architecture

```
retail-data-engineering-project
│
├── data
│   ├── retail_dataset.csv
│   └── transformed_retail.csv
│
├── scripts
│   ├── ingest_data.py
│   ├── clean_data.py
│   ├── feature_engineering.py
│   ├── database_load.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── ml_models.py
│   └── pipeline.py
│
├── logs
│   └── pipeline.log
│
└── README.md
```

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* MySQL
* VS Code

---

# Dataset Information

The dataset contains **retail transaction records** including:

* Invoice
* StockCode
* Description
* Quantity
* InvoiceDate
* Price
* Customer ID
* Country

Total Records: **500,000+**

---

# Data Engineering Pipeline

The pipeline consists of the following stages:

### 1️⃣ Data Ingestion

Loads raw retail data into the pipeline.

### 2️⃣ Data Cleaning

Handles missing values and removes invalid records.

### 3️⃣ Feature Engineering

Creates new features such as:

* Month
* TotalAmount

### 4️⃣ Database Storage

Stores processed data in a **MySQL database**.

### 5️⃣ Data Analysis

Performs exploratory analysis on sales data.

### 6️⃣ Data Visualization

Generates charts to understand:

* Monthly sales trends
* Country-wise sales
* Product demand

### 7️⃣ Machine Learning Models

Regression Models:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Support Vector Regression

Classification Model:

* Naive Bayes (Sales Category Prediction)

---

# Automation Pipeline

The entire workflow is automated using a **Python pipeline script**.

Run the full pipeline with:

```
python scripts/pipeline.py
```

This will execute all steps sequentially.

---

# Logging System

Pipeline logs are saved in:

```
logs/pipeline.log
```

Logs help track pipeline execution and errors.

---

# Sample Output

Example model results:

Linear Regression
R2 Score: 0.66

Decision Tree
R2 Score: 0.74

Random Forest
R2 Score: 0.75

Naive Bayes
Accuracy: 0.99

---

# Project Highlights

* End-to-end **Data Engineering pipeline**
* Automated ETL workflow
* Data analysis and visualization
* Multiple machine learning models
* Logging and error handling

---

