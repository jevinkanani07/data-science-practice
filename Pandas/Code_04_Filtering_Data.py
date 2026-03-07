# Pandas Code 04
# Topic: Filtering Data

import pandas as pd

# Create dataset
data = {
    "Name": ["Jevin", "Rahul", "Amit", "Neha", "Priya"],
    "Age": [19, 21, 20, 22, 23],
    "Marks": [85, 90, 78, 88, 95]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("----------------------")

# Filter students with marks > 85
high_marks = df[df["Marks"] > 85]

print("Students with marks > 85:")
print(high_marks)

print("----------------------")

# Filter students with age > 20
age_filter = df[df["Age"] > 20]

print("Students with age > 20:")
print(age_filter)

print("----------------------")

# Multiple conditions
filtered = df[(df["Marks"] > 80) & (df["Age"] > 20)]

print("Students with Marks > 80 and Age > 20:")
print(filtered)