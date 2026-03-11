# Code 09
# Topic: Data Visualization using Pandas and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Name": ["Jevin", "Bhavesh", "vivan", "yash", "nikunj"],
    "Marks": [85, 78, 92, 74, 88]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("-------------------")

# Line Chart
plt.plot(df["Name"], df["Marks"], marker='o')
plt.title("Students Marks Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

print("-------------------")

# Bar Chart
plt.bar(df["Name"], df["Marks"])
plt.title("Students Marks Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
