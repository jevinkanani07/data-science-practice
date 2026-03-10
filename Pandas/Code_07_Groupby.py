# Pandas Code 07
# Topic: GroupBy and Aggregation

import pandas as pd

# Create dataset
data = {
    "Department": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
    "Employee": ["Jevin", "Rahul", "Amit", "Neha", "Priya", "Karan"],
    "Salary": [60000, 65000, 50000, 52000, 70000, 72000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("----------------------")

# Group by Department and calculate mean salary
group_mean = df.groupby("Department")["Salary"].mean()

print("Average Salary by Department:")
print(group_mean)

print("----------------------")

# Sum of salaries
group_sum = df.groupby("Department")["Salary"].sum()

print("Total Salary by Department:")
print(group_sum)

print("----------------------")

# Count employees per department
group_count = df.groupby("Department")["Employee"].count()

print("Employee Count by Department:")
print(group_count)

print("----------------------")

# Multiple aggregation
group_stats = df.groupby("Department")["Salary"].agg(["mean", "max", "min"])

print("Salary statistics by Department:")
print(group_stats)