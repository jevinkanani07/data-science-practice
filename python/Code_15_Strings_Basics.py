# Code 15
# Topic: Strings in Python (Basics)

# Create a string
text = "Data Science"
print("Text:", text)

# Length of string
print("Length:", len(text))

# Indexing
print("First character:", text[0])
print("Last character:", text[-1])

# Slicing
print("First 4 characters:", text[0:4])
print("From index 5 to end:", text[5:])

# Loop through string
print("Characters in string:")
for ch in text:
    print(ch)

print("----------------")

# Check substring
print("Is 'Data' in text?", "Data" in text)
print("Is 'Python' in text?", "Python" in text)