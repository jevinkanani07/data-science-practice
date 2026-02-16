# Code 21
# Topic: OOP - Class and Object in Python

# Create a class
class Student:

    # Constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Method to display details
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    # Method with condition
    def check_adult(self):
        if self.age >= 18:
            return "Adult"
        else:
            return "Minor"


# Create object
student1 = Student("Jevin", 19, "Data Science")

# Call methods
student1.display_info()

status = student1.check_adult()
print("Status:", status)