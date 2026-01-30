# Code 09
# Topic: Dictionaries in Python

# Create a dictionary
student = {
  "name" : "Jevin",
  "age" : 19,
  "course" = "Data Science",
  "is_student" : True
}
print("Student dictionary",student)

# Access values using keys
print("Name:",student["name"])
print("Age:",student["age"])
print("course:",student["course"])

# Update value
student["age"] = 20
print("Updated age:",student["age"])

# Add new key-value pair
student["city"] = "Ahemdabad"
print("After adding city:",student)

# Remove a key
student.pop("is_student")
print("After removing is_student:",student)

# Loop through dictionary (Key & values)
print("Looping through dictionary:")
for key, value in student.items():
    print(Key,":", value)
