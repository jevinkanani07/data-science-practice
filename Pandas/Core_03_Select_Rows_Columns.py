# Pandas Code 03
# Topic: Selecting Rows and Columns

import pandas as pd

# Create sample dataset
data = {
    "Name": ["Jevin", "Rahul", "Amit", "Neha"],
    "Age": [19, 21, 20, 22],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("----------------------")

# Select single column
print("Names column:")
print(df["Name"])

print("----------------------")

# Select multiple columns
print("Name and Marks:")
print(df[["Name", "Marks"]])

print("----------------------")

# Select row using loc
print("Row with index 1:")
print(df.loc[1])

print("----------------------")

# Select rows using iloc
print("First two rows:")
print(df.iloc[0:2])

print("----------------------")

# Specific value
print("Marks of Amit:")
print(df.loc[2, "Marks"])