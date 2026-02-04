# Code 12
# Topic : Function with Lists and Loops

# Function to calculate total marks
def calculate_total(marks):
    total = 0
    for m in marks:
        total += m
    return total

# Function to calculate average marks
def calculate_average(marks):
    total = calculate_total(marks)
    avg = total / len(marks)
    return avg

# List of marks
marks_list = [70, 85, 90, 60, 75]

print("Marks list:", marks_list)

# Call function
total_marks = calculate_total(marks_list)
average_marks = calculate_average(marks_list)

print("Total marks:", total_marks)
print("Average marks:",average_marks)

# Function with condition + loop
def count_pass_students(marks):
    count = 0
  for m in marks:
      if m >= 40:
          count += 1
      return count

pass_count = count_pass_student(marks_list)
print("Number os passed students:",pass_count)
