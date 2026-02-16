# Code 20
# Topic: File Handling in Python

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is Day 20.\n")
    file.write("Learning File Handling in Python.\n")

print("File written successfully.")

print("-------------------")

# Reading from the file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

print("-------------------")

# Appending to the file
with open("sample.txt", "a") as file:
    file.write("This line is appended later.\n")

print("Data appended successfully.")

print("-------------------")

# Reading again to confirm append
with open("sample.txt", "r") as file:
    print("Updated file content:")
    print(file.read())