# Code 08
# Topic: Merge DataFrames

import pandas as pd

# First DataFrame (Employee details)
employee_data = {
    "Emp_ID": [1, 2, 3, 4],
    "Name": ["Jevin", "bhavesh", "vivan", "nikunj"]
}

df_employee = pd.DataFrame(employee_data)

print("Employee Data")
print(df_employee)

print("------------------")

# Second DataFrame (Salary details)
salary_data = {
    "Emp_ID": [1, 2, 3, 4],
    "Salary": [60000, 55000, 50000, 62000]
}

df_salary = pd.DataFrame(salary_data)

print("Salary Data")
print(df_salary)

print("------------------")

# Merge DataFrames
merged_df = pd.merge(df_employee, df_salary, on="Emp_ID")

print("Merged DataFrame")
print(merged_df)
