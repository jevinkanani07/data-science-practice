# Pandas Code 06
# Topic: Handling Missing Values

import pandas as pd
import numpy as np

# Create dataset with missing values
data = {
    "Name": ["Jevin", "Rahul", "Amit", "Neha", "Priya"],
    "Age": [19, np.nan, 20, 22, np.nan],
    "Marks": [85, 90, np.nan, 88, 95]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("----------------------")

# Check missing values
print("Missing values:")
print(df.isnull())

print("----------------------")

# Count missing values
print("Missing value count:")
print(df.isnull().sum())

print("----------------------")

# Drop rows with missing values
drop_df = df.dropna()

print("After dropping missing rows:")
print(drop_df)

print("----------------------")

# Fill missing values
fill_df = df.fillna(0)

print("After filling missing values with 0:")
print(fill_df)

print("----------------------")

# Fill with column mean
df["Age"].fillna(df["Age"].mean(), inplace=True)

print("After filling Age with mean:")
print(df)