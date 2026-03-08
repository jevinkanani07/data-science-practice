# Pandas Code 05
# Topic: Sorting Data and Reset Index

import pandas as pd

# Create dataset
data = {
    "Name": ["Jevin", "Rahul", "Amit", "Neha", "Priya"],
    "Age": [19, 21, 20, 22, 23],
    "Marks": [85, 90, 78, 88, 95]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("----------------------")

# Sort by Marks (ascending)
sorted_marks = df.sort_values(by="Marks")

print("Sorted by Marks (ascending):")
print(sorted_marks)

print("----------------------")

# Sort by Marks (descending)
sorted_marks_desc = df.sort_values(by="Marks", ascending=False)

print("Sorted by Marks (descending):")
print(sorted_marks_desc)

print("----------------------")

# Sort by multiple columns
multi_sort = df.sort_values(by=["Age", "Marks"])

print("Sorted by Age then Marks:")
print(multi_sort)

print("----------------------")

# Reset index
reset_df = sorted_marks_desc.reset_index(drop=True)

print("After resetting index:")
print(reset_df)