# Code 19
# Topic: Exception Handling in Python

# Example 1: Zero Division Error
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid integers!")

else:
    print("Calculation successful!")

finally:
    print("Program finished.")
    

print("----------------------")

# Example 2: Accessing list index
numbers = [10, 20, 30]

try:
    print("Accessing element:", numbers[5])

except IndexError:
    print("Error: Index out of range!")

finally:
    print("List operation complete.")
