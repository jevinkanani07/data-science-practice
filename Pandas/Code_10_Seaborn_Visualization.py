# Code 10
# Topic: Data Visualization using Seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Name": ["Jevin", "Rahul", "Amit", "Neha", "Priya"],
    "Marks": [85, 78, 92, 74, 88],
    "Hours_Study": [5, 4, 6, 3, 5]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("----------------")

# Bar Plot
sns.barplot(x="Name", y="Marks", data=df)

plt.title("Students Marks Bar Plot")
plt.show()

print("----------------")

# Scatter Plot
sns.scatterplot(x="Hours_Study", y="Marks", data=df)

plt.title("Study Hours vs Marks")
plt.show()
