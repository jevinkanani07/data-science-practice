# Code 24
# Mini Project: Student Result System

def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"

# User input
name = input("Enter student name: ")

marks = []
for i in range(3):
    score = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(score)

# Calculations
total = calculate_total(marks)
average = calculate_average(marks)
grade = calculate_grade(average)

# Store result in dictionary
result = {
    "Name": name,
    "Marks": marks,
    "Total": total,
    "Average": average,
    "Grade": grade
}

print("\n----- Student Result -----")
for key, value in result.items():
    print(key, ":", value)