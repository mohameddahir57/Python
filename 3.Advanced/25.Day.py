# Day 25 : Working with Databases (SQLite CRUD) 
# Welcome to Day 25 of your Python learning journey! Today, we will explore how to work with databases using SQLite in Python. We will cover the basics of creating, reading, updating, and deleting (CRUD) records in a SQLite database.
# SQLite is a lightweight, disk-based database that doesn't require a separate server process. Python has built-in support for SQLite through the `sqlite3` module.
# Table of Contents
# 1. [Creating a Database](#creating-a-database)
# 2. [Creating a Table](#creating-a-table)
# 3. [Inserting Data](#inserting-data)
# 4. [Reading Data](#reading-data)
# 5. [Updating Data](#updating-data)
# 6. [Deleting Data](#deleting-data)
# 7. [Closing the Database](#closing-the-database)
# 8. [Practice Exercises](#practice-exercises)

# Creating a Database
# You can create a SQLite database using the `sqlite3` module. If the database file does not exist, it will be created.
import sqlite3
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Creating a Table
# You can create a table in the database using the `CREATE TABLE` SQL command.
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
connection.commit()


# Inserting Data
# You can insert data into the table using the `INSERT INTO` SQL command.
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
connection.commit()

# Reading Data
# You can read data from the table using the `SELECT` SQL command.
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
# Output:
# (1, 'Alice', 30)
# (2, 'Bob', 25)

# Updating Data
# You can update data in the table using the `UPDATE` SQL command.
cursor.execute("UPDATE users SET age = 31 WHERE name = 'Alice'")
connection.commit()

# Deleting Data
# You can delete data from the table using the `DELETE` SQL command.
cursor.execute("DELETE FROM users WHERE name = 'Bob'")
connection.commit()

# Closing the Database
# After you are done working with the database, you should close the connection.
connection.close()

# Practice Exercises
# 1. Create a new table called `products` with columns `id`, `name`, and `price`.
import sqlite3
connection = sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS products
                    (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
connection.commit()
connection.close()

# 2. Insert at least three products into the `products` table.
connection = sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute("INSERT INTO products (name, price) VALUES ('Laptop', 1200)")
cursor.execute("INSERT INTO products (name, price) VALUES ('Smartphone', 800)")
cursor.execute("INSERT INTO products (name, price) VALUES ('Tablet', 400)")
connection.commit()
connection.close()

# 3. Query and print all products from the `products` table.
connection = sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.close()
# Output:
# (1, 'Laptop', 1200.0)
# (2, 'Smartphone', 800.0)
# (3, 'Tablet', 400.0)


# 4. Update the price of one product in the `products` table.
connection = sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute("UPDATE products SET price = 1000 WHERE name = 'Laptop'")
connection.commit()
connection.close()

# 5. Delete one product from the `products` table.
connection = sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute("DELETE FROM products WHERE name = 'Smartphone'")
connection.commit()
connection.close()

# Output:
# (1, 'Laptop', 1200.0)
# (2, 'Smartphone', 800.0)
# (3, 'Tablet', 400.0)
# 1000


class ReverseStringIterator:
    def __init__(self, string):
        self.string = string
        self.index = len(string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            char = self.string[self.index]
            self.index -= 1
            return char
        else:
            raise StopIteration

reverse_iterator = ReverseStringIterator("Hello")
for char in reverse_iterator:
    print(char)
# Output:
# o
# l
# l
# e
# H
# Hello
# e
# l
# l
# o
# H
#  l
# l
#  e
# Hello


