# Code 22
# Topic: OOP - Inheritance and Encapsulation

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child class (Inheritance)
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)   # Call parent constructor
        self.course = course

    def show_course(self):
        print("Course:", self.course)


# Encapsulation example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def get_balance(self):
        return self.__balance


# Using Inheritance
student1 = Student("Jevin", 19, "Data Science")
student1.display()
student1.show_course()

print("----------------")

# Using Encapsulation
account = BankAccount(1000)
account.deposit(500)
print("Current Balance:", account.get_balance())