# Code 23
# Topic: OOP - Polymorphism and Method Overriding

# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")


# Child class 1
class Dog(Animal):
    def sound(self):  # Method overriding
        print("Dog barks")


# Child class 2
class Cat(Animal):
    def sound(self):  # Method overriding
        print("Cat meows")


# Polymorphism example using function
def make_sound(animal):
    animal.sound()


# Create objects
animal = Animal()
dog = Dog()
cat = Cat()

# Direct calls
animal.sound()
dog.sound()
cat.sound()

print("----------------")

# Using polymorphism
make_sound(dog)
make_sound(cat)