# NumPy Code 10
# Mini Project: Student Marks Analysis

import numpy as np

# Student marks (rows = students, columns = subjects)
marks = np.array([
    [85, 90, 78],
    [70, 88, 92],
    [60, 75, 80],
    [95, 85, 91],
    [50, 65, 70]
])

print("Marks Matrix:\n", marks)

print("----------------------")

# Average marks per student
student_avg = np.mean(marks, axis=1)
print("Average marks per student:", student_avg)

print("----------------------")

# Average marks per subject
subject_avg = np.mean(marks, axis=0)
print("Average marks per subject:", subject_avg)

print("----------------------")

# Highest marks
print("Highest mark:", np.max(marks))

# Lowest marks
print("Lowest mark:", np.min(marks))

print("----------------------")

# Students who scored above 85 in any subject
high_scores = marks[marks > 85]
print("Marks greater than 85:", high_scores)

print("----------------------")

# Total marks per student
total_marks = np.sum(marks, axis=1)
print("Total marks per student:", total_marks)