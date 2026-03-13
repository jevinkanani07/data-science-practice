# Code 13
# Topic: Feature Engineering

import pandas as pd

# Create dataset
data = {
    "Name": ["Jevin", "Rahul", "Amit", "Neha", "Priya"],
    "Marks": [85, 78, 92, 74, 88],
    "Hours_Study": [5, 4, 6, 3, 5]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("----------------------")

# Create new feature (Marks per study hour)
df["Marks_per_Hour"] = df["Marks"] / df["Hours_Study"]

print("After creating new feature:")
print(df)

print("----------------------")

# Create category column using condition
df["Performance"] = df["Marks"].apply(
    lambda x: "Excellent" if x >= 90 else
              "Good" if x >= 80 else
              "Average"
)

print("After adding Performance column:")
print(df)
