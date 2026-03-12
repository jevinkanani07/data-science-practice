# Code 12
# Topic: Exploratory Data Analysis (EDA)

import pandas as pd

# Create dataset
data = {
    "Name": ["Jevin", "Rahul", "Amit", "Neha", "Priya"],
    "Marks": [85, 78, 92, 74, 88],
    "Hours_Study": [5, 4, 6, 3, 5],
    "Attendance": [90, 85, 95, 80, 88]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("----------------------")

# Basic info
print("Dataset Info:")
print(df.info())

print("----------------------")

# Summary statistics
print("Summary Statistics:")
print(df.describe())

print("----------------------")

# Unique values
print("Unique study hours:")
print(df["Hours_Study"].unique())

print("----------------------")

# Value counts
print("Study hours count:")
print(df["Hours_Study"].value_counts())
