#Day 21-Advanced OOP (inheritance, polymorphism, decorators)
#Welcome to Day 21 of your Python learning journey! Today, we will explore Advanced OOP in Python, including inheritance, polymorphism, and decorators. These concepts help you write more efficient and modular code by reusing and extending existing classes.
## Table of Contents
#1. [Inheritance](#inheritance)
#2. [Polymorphism](#polymorphism)
#3. [Decorators](#decorators)
#4. [Practice Exercises](#practice-exercises)

## Inheritance
#Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
#The child class can then add or modify the attributes and methods inherited from the parent class.
#The child class is said to be a subclass of the parent class, and the parent class is said to be a superclass of the child class.
#Inheritance is a fundamental concept in object-oriented programming that helps in creating a hierarchy of classes.

class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

dog_instance = Dog()
print(dog_instance.speak())  # Output: Bark 


## Polymorphism
#Polymorphism refers to the ability of objects of different classes to respond to the same message in different ways.
#In Python, polymorphism is achieved through method overloading and method overriding.
#Method overloading allows a class to have multiple methods with the same name but different parameters.
#Method overriding allows a subclass to provide a different implementation of a method inherited from the parent class.

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

my_rectangle = Rectangle(5, 3)
print(my_rectangle.area())  # Output: 15


## Decorators
#Decorators are functions that modify the behavior of another function. They are often used to add additional functionality to a function without modifying the function itself.
#Decorators are defined using the `@` symbol followed by the decorator function name.
#The `@` symbol is used to indicate that the following function is a decorator.
#Code Example

def decorator_function(func):
    def wrapper_function(*args, **kwargs):
        # Do something before the function is called
        result = func(*args, **kwargs)
        # Do something after the function is called
        return result
    return wrapper_function

@decorator_function
def my_function():
    print("This is my function")

my_function()


#practice-exercises

#1. Write a class `Person` with attributes `name` and `age`. Include a method `introduce` that prints a message introducing the person.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person_instance = Person("John", 30)
print(person_instance.introduce())


#2. Define a class `Rectangle` with attributes `length` and `width`. Include methods `area` and `perimeter` to calculate the area and perimeter of the rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)   

rectangle_instance = Rectangle(5, 3)
print(rectangle_instance.area())  # Output: 15
print(rectangle_instance.perimeter())  # Output: 16


#3. Create a class `Car` with attributes `make`, `model`, and `year`. Include a method `display_info` that prints the make, model, and year of the car.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

car_instance = Car("Toyota", "Camry", 2022)
print(car_instance.display_info())  # Output: 2022 Toyota Camry

