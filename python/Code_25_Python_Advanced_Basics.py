# Code 25
# Topic: Advanced Python Basics

# Lambda function
square = lambda x: x * x
print("Square of 5:", square(5))

print("------------------")

# Using map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("Squares using map:", squares)

print("------------------")

# Using filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", even_numbers)

print("------------------")

# List comprehension
squares_lc = [x * x for x in numbers]
print("Squares using list comprehension:", squares_lc)

print("------------------")

# Combine condition + comprehension
even_squares = [x * x for x in numbers if x % 2 == 0]
print("Even squares:", even_squares)