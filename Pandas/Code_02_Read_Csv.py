# Pandas Code 02
# Topic: Reading CSV File

import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

print("Dataset:")
print(df)

print("----------------------")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

print("----------------------")

# Show last 5 rows
print("Last 5 rows:")
print(df.tail())

print("----------------------")

# Dataset information
print("Dataset Info:")
print(df.info())

print("----------------------")

# Shape of dataset
print("Dataset shape:", df.shape)