#Day 10 - Object-Oriented Programming (OOP): Learn class, object, methods, `__init__`, and inheritance in Python.
#Welcome to Day 10 of your Python learning journey! Today, we will explore Object-Oriented Programming (OOP) in Python. OOP is a programming paradigm that uses "objects" to represent data and methods to manipulate that data. This approach helps in organizing code, making it more modular, reusable, and easier to maintain.
## Table of Contents
#1. [Classes and Objects](#classes-and-objects)
#2. [Methods](#methods)
#3. [The `__init__` Method](#the-__init__-method)
#4. [Inheritance](#inheritance) 

## Classes and Objects
#A class is a blueprint for creating objects. An object is an instance of a class.
class Moha:
    def speak(self):
        return "Hello, I am Moha!"
moha_instance = Moha()
print(moha_instance.speak())  # Output: Hello, I am Moha!

## Methods
#Methods are functions defined within a class that operate on the object's data.
class Moha:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"Hello, I am {self.name}!"
moha_instance = Moha("Moha")
print(moha_instance.speak())  # Output: Hello, I am Moha!

## The `__init__` Method
#The `__init__` method is a special method called a constructor that initializes an object's attributes when the object is created.
class Moha:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
moha_instance = Moha("Moha", 5)
print(moha_instance.introduce())  # Output: My name is Moha and I am 5 years old.

## Inheritance
#Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog_instance = Dog()
cat_instance = Cat()
print(dog_instance.speak())  # Output: Bark
print(cat_instance.speak())  # Output: Meow

## Practice Exercises
#1. Define a class `Car` with attributes `make`, `model`, and `year`. Include a method `display_info` that prints the car's details.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.display_info())  # Output: 2020 Toyota Corolla

#2. Create a class `Rectangle` with attributes `length` and `width`. Add a method `area` that returns the area of the rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
my_rectangle = Rectangle(5, 3)
print(my_rectangle.area())  # Output: 15

#3. Define a class `Person` with attributes `name` and `age`. Create a subclass `Student` that inherits from `Person` and adds an attribute `student_id`. Include a method `introduce` in both classes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}."
student_instance = Student("Alice", 20, "S12345")
print(student_instance.introduce())  # Output: My name is Alice, I am 20 years old, and my student ID is S12345.

#4. Create a class `BankAccount` with attributes `account_number` and `balance`. Include methods `deposit` and `withdraw` to modify the balance.
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"
my_account = BankAccount("123456789")
print(my_account.deposit(500))  # Output: 500
print(my_account.withdraw(200))  # Output: 300
print(my_account.withdraw(400))  # Output: Insufficient funds
    
#5. Define a class `Employee` with attributes `name`, `position`, and `salary`. Create a method `give_raise` that increases the salary by a given percentage.
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)
        return self.salary  
employee_instance = Employee("Bob", "Developer", 60000)
print(employee_instance.give_raise(10))  # Output: 66000.0
#6. Create a class `Library` that contains a list of books. Include methods to add a book, remove a book, and display all books.
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def display_books(self):
        return self.books
my_library = Library()
my_library.add_book("1984 by George Orwell")
my_library.add_book("To Kill a Mockingbird by Harper Lee")
print(my_library.display_books())  # Output: ['1984 by George Orwell', 'To Kill a Mockingbird by Harper Lee']
my_library.remove_book("1984 by George Orwell")
print(my_library.display_books())  # Output: ['To Kill a Mockingbird by Harper Lee']
def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))
odd_numbers = filter_even_numbers([1, 2, 3, 4, 5, 6])
print(odd_numbers)  # Output: [1, 3, 5]


#Congratulations on completing Day 10! You have learned the fundamentals of Object-Oriented Programming in Python, including classes, objects, methods, the `__init__` method, and inheritance. Keep practicing by creating your own classes and exploring more advanced OOP concepts like polymorphism and encapsulation. Happy coding!