![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-025E8C?style=for-the-badge)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

# healthcare-business-insights
A complete Healthcare Data Analysis project demonstrating the end-to-end analytics workflow—from data cleaning and feature engineering in Python to SQL analysis in PostgreSQL and interactive reporting in Power BI.

## 📌 Project Overview

Healthcare organizations generate large volumes of patient, hospital, and billing data every day. This project focuses on preparing raw healthcare data, storing it in a relational database, performing business analysis using SQL, and building an interactive Power BI dashboard to support data-driven decision-making.

This project follows a complete ETL and Business Intelligence workflow:

```
Raw Dataset
      │
      ▼
Python
(Data Cleaning & Feature Engineering)
      │
      ▼
PostgreSQL
(Data Loading & Storage)
      │
      ▼
SQL
(Business Analysis)
      │
      ▼
Power BI
(Interactive Dashboard & Insights)
```

---

# 🎯 Objectives

- Clean and preprocess raw healthcare data.
- Perform feature engineering to improve analysis.
- Load processed data into PostgreSQL using Python.
- Analyze healthcare data using SQL.
- Build an interactive Power BI dashboard.
- Generate meaningful business insights from patient and hospital data.

---

# 🛠️ Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **PostgreSQL**
- **SQL**
- **Power BI**
- **DAX**
- **Git & GitHub**

---

# 📂 Project Structure

```
Healthcare-Analytics-Dashboard
│
├── data
│   ├── healthcare_raw.csv
│   └── healthcare_cleaned.csv
│
├── notebooks
│   └── healthcare_analysis.ipynb
│
├── sql
│   └── healthcare_queries.sql
│
├── powerbi
│   └── Healthcare_Analytics_Dashboard.pbix
│
├── dashboard
│   └── dashboard_preview.png
│
├── README.md
└── requirements.txt
```

---

# 📊 Dataset

The dataset contains healthcare information including:

- Patient Details
- Age & Gender
- Blood Type
- Medical Condition
- Admission Details
- Discharge Details
- Doctors
- Hospitals
- Insurance Providers
- Billing Amount
- Medication
- Test Results

---

# 🧹 Data Cleaning (Python)

The following preprocessing steps were performed:

- Removed duplicate records
- Checked and handled missing values
- Converted data types
- Converted date columns to datetime
- Converted categorical columns
- Cleaned string values
- Validated dataset quality

---

# ⚙️ Feature Engineering

Seven new features were created:

| Feature | Description |
|----------|-------------|
| Length_of_Stay | Days between admission and discharge |
| Admission_Year | Extracted from admission date |
| Admission_Month | Extracted from admission date |
| Admission_Day | Extracted from admission date |
| Admission_Quarter | Quarter of admission |
| Age_Group | Categorized patient age |
| Billing_Category | Billing amount category |

---

# 🗄️ PostgreSQL

The cleaned dataset was loaded directly into PostgreSQL using Python (`SQLAlchemy` + `psycopg2`) to simulate a simple ETL workflow.

---

# 📈 SQL Analysis

Business-focused SQL queries were written to analyze:

- Total Patients
- Total Revenue
- Average Billing Amount
- Average Length of Stay
- Patient Distribution by Gender
- Patient Distribution by Age Group
- Medical Condition Analysis
- Admission Type Analysis
- Revenue by Hospital
- Revenue by Insurance Provider
- Average Billing by Medical Condition
- Monthly Admissions
- Quarterly Admissions
- Top Doctors by Patient Count
- Top Hospitals by Patient Count

---

# 📊 Power BI Dashboard

The Power BI dashboard provides an interactive overview of healthcare performance through:

### KPI Cards

- Total Patients
- Total Revenue
- Average Billing
- Average Length of Stay
- Average Age
- Total Hospitals

### Visualizations

- Patients by Medical Condition
- Revenue by Hospital
- Revenue by Insurance Provider
- Admission Type Distribution
- Blood Type Distribution
- Monthly Admission Trend
- Patient Distribution by Age Group

### Interactive Filters

- Gender
- Hospital
- Doctor
- Insurance Provider
- Medical Condition
- Admission Type
- Admission Month

---

# 💡 Key Insights

- Identified the most common medical conditions.
- Compared hospital performance based on patient volume.
- Analyzed billing trends across hospitals.
- Evaluated insurance provider contributions.
- Examined monthly admission patterns.
- Measured average patient length of stay.

---

# 🚀 Skills Demonstrated

- Data Cleaning
- Data Preprocessing
- Feature Engineering
- ETL Workflow
- PostgreSQL Integration
- SQL Query Writing
- Business Analysis
- Power BI Dashboard Development
- DAX Measures
- Data Visualization

---

# 📌 Future Improvements

- Add multiple fact and dimension tables
- Build a star schema data model
- Include advanced DAX measures
- Publish the dashboard to Power BI Service
- Automate data refresh

---

# 👩‍💻 Author

**Shafiya Naaz Shaikh**

Aspiring Data Analyst | Python | SQL | PostgreSQL | Power BI

Connect with me on LinkedIn and feel free to explore my other analytics projects.
