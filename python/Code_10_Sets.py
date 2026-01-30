# Code 10
# Topic : Sets in Python

# Create a set
numbers = {1,2,3,4,5}
print("Numbers set:",numbers)

# Remove element
numbers.remove(2)
print("After remove: ", numbers)

# cheack element 
print("Is 3 in set?", 3 in numbers)

# Another set
even_numners = {2,4,6,8}

# Set operations
print("Union:",numbers.union(even_numbers))
print("Intersection",numbers.intersection(even_numbers))
print("Difference",numbers.difference(even_numbers))

# Loop through set
print("Looping through set:")
for num in numbers:
    print(num)
