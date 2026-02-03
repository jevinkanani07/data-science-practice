# Code 11
# Topic : Functions in python

# simple function 
def greet():
    print("Hello, Welcome")

greet()

print("---- ")

# Function with parameters
def student_info(name, age):
    print("Name:",name)
    print("Age:",age)

student_info("Jevin", 19)

print("-----")

# Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(10,5)
print("Sum:",result)

# Function with coundition
def check_pass(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

status = check_pass(75)
print("Result:", status)
