# Code 16
# Topic: String Methods in Python

text = "  Data Science with Python  "

print("Original text:", text)

# Remove extra spaces
clean_text = text.strip()
print("After strip:", clean_text)

# Convert case
print("Upper case:", clean_text.upper())
print("Lower case:", clean_text.lower())

# Replace word
new_text = clean_text.replace("Python", "Machine Learning")
print("After replace:", new_text)

# Split string
words = clean_text.split(" ")
print("Split into words:", words)

# Join list into string
joined_text = "-".join(words)
print("Joined text:", joined_text)

# Count occurrences
print("Count of 'a':", clean_text.count("a"))

# Startswith / Endswith
print("Starts with 'Data'?", clean_text.startswith("Data"))
print("Ends with 'Python'?", clean_text.endswith("Python"))