# Code 13
# Topic : user Input with Functions

# Function to greet user
def greet_user(name):
    print("Hello",name,"Welcome to Python Leraning")

# Function to Calculate square
def calculate_square(num):
    return num*num

# Taking user input
user_name = input("Enter your name:")
greet_user(user_name)

print("----")

number = int(input("Enter a number:"))
square = calculate_square(number)
print("Square of",number,"is:",square)

print("-----")

# Function with condition 
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = check_even_odd(number)
print("The number is:",result)
