
import pandas as pd 
import numpy as np
df=pd.read_csv("healthcare_raw.csv")
print(df.head(5))

#STEP 2 Initial Inspection

print(df.tail(5))
print(df.info())
print(df.describe())

print(df.isnull().sum())

#STEP 3 Data Quality Check

print('duplicates')
print(df.duplicated().sum())

print('null')
print(df.isnull().sum())

print('unique')
print(df.nunique())

print('value_counts')
print(df.value_counts('Gender'))
print(df.value_counts('Medical Condition'))
print(df.value_counts('Insurance Provider'))
print(df.value_counts('Medication'))
print(df.value_counts('Test Results'))

#STEP 4 Data Cleaning
df = df.drop_duplicates()
print('duplicates')
print(df.duplicated().sum())

print('null')
print(df.isnull().sum())

print('data type')
print(df.dtypes)

df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
print(df.dtypes)

category_columns = [
    'Gender',
    'Blood Type',
    'Medical Condition',
    'Insurance Provider',
    'Admission Type',
    'Medication',
    'Test Results'
]

for col in category_columns:
    df[col] = df[col].astype('category')


print(df.dtypes)

# STEP 5 Clean String Column 

df["Name"] = (
    df["Name"]
    .astype("string")
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
    .str.title()
)

print(df["Name"].head(5))

print(df.head(5))

# STEP 6 Feature Engineering

df["Lenght_of_stay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days

print(df.head(5))


df["Admission_Year"] = df["Date of Admission"].dt.year
df["Admission_Month"] = df["Date of Admission"].dt.month_name()
df["Admission_Quarter"] = "Q" + df["Date of Admission"].dt.quarter.astype(str)

bins = [0, 18, 35, 50, 65, 120]
labels = ["Child", "Young Adult", "Adult", "Middle Age", "Senior"]

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels,
    include_lowest=True
)
df["Billing_Category"] = pd.qcut(
    df["Billing Amount"],
    q=3,
    labels=["Low", "Medium", "High"]
)

#STEP 7 Final Validation
print(df.head(5))
print(df.isnull().sum())
print("no duplicates")
df.duplicated().sum()
df.describe(include="all")

#STEP 8 Save Cleaned Data
df.to_csv("healthcare_cleaned.csv", index=False)
print("Data cleaned and saved to healthcare_cleaned.csv")

#STEP 9 Database Connection
from sqlalchemy import create_engine

# PostgreSQL Connection Details
username = "postgres"
password = "postdb02"
host = "localhost"
port = "5432"
database = "sql_project_p1"

# Create Connection Engine
engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

print("✅ Connected to PostgreSQL Successfully!")

df.to_sql(
    "healthcare_cleaned",
    con=engine,
    if_exists="replace",
    index=False
)