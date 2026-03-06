# Pandas Code 01
# Topic: Introduction to Pandas and DataFrame

import pandas as pd

# Create a Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print("Pandas Series:")
print(series)

print("----------------------")

# Create DataFrame using dictionary
student_data = {
    "Name": ["Jevin", "Rahul", "Amit"],
    "Age": [19, 21, 20],
    "Course": ["Data Science", "AI", "Machine Learning"]
}

df = pd.DataFrame(student_data)

print("DataFrame:")
print(df)

print("----------------------")

# DataFrame information
print("Shape of DataFrame:", df.shape)

print("Columns:", df.columns)

print("Data types:")
print(df.dtypes)