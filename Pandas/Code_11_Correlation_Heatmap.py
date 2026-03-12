# Code 11
# Topic: Correlation Heatmap using Seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Marks": [85, 78, 92, 74, 88],
    "Hours_Study": [5, 4, 6, 3, 5],
    "Attendance": [90, 85, 95, 80, 88]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("----------------")

# Correlation matrix
corr = df.corr()

print("Correlation Matrix:")
print(corr)

print("----------------")

# Heatmap
sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()
