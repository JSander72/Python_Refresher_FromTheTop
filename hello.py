# 1. Print statement - Used to output text or variables to the console
print("Hello, World!")

# 2. Variables and Data Types
x = 10  # Integer | integers are whole numbers
y = 3.14  # Float | floats are numbers with decimal points
z = 5 + 2j  # Complex number | complex numbers are numbers with real and imaginary parts
name = "James"  # String | strings are sequences of characters
is_active = True  # Boolean | booleans are True or False values

# 3. Conditional Statements | Used to perform different actions based on different conditions
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less") #output: x is greater than 5

# 4. Loops | Used to execute a block of code repeatedly
# For loop | Used to iterate over a sequence (like a list, tuple, or string)
for i in range(5):  # Loops from 0 to 4
    print(i) # Output: 0 1 2 3 4

# While loop | Used to execute a block of code as long as a condition is true
count = 0
while count < 5:
    print(count) # Output: 0 1 2 3 4
    count += 1

# 5. Functions | Used to encapsulate code into reusable blocks | Functions are defined using the "def" keyword
def greet(name):
    """This function greets the person with the given name."""
    return f"Hello, {name}!"

print(greet("James")) # Output: Hello, James!

# 6. Lists | Used to store multiple items in a single variable | Lists are ordered and mutable | Ordered means the items have a defined order, and mutable means you can change the list after it is created
# Lists can contain different data types
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Accessing elements
fruits.append("date")  # Adding an element
print(fruits)
    #output: ['apple', 'banana', 'cherry', 'date']

# 7. Dictionaries | Used to store data values in key:value pairs | Dictionaries are unordered, changeable, and indexed
# Dictionaries are used to store data values in key:value pairs
# A dictionary is a collection which is unordered, changeable and indexed
# Dictionaries are written with curly brackets, and they have keys and values
person = {"name": "James", "age": 30}
print(person["name"])  # Accessing values | Output: James
person["age"] = 31  # Modifying values
print(person) # Output: {'name': 'James', 'age': 31}

# 8. Classes and Objects | Used to create user-defined data structures | Classes are blueprints for creating objects
# Objects are instances of classes
# A class is a code template used to create objects. Objects are instances of classes.
# Classes encapsulate data for the object and methods to manipulate that data
class Person:
    """A simple class to represent a person."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

james = Person("James", 30)
print(james.introduce()) # Output: My name is James and I am 30 years old.

# 9. Exception Handling | Used to handle errors gracefully | Exceptions are events that can modify the flow of control through a program
# Exception handling is a construct in some programming languages to handle or deal with errors automatically.
# It is a way to transfer control from one part of the code to another.
# It is a way to handle errors gracefully without crashing the program
# try and except blocks are used to catch and handle exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!") # Output: You can't divide by zero!

# 10. Importing Modules | Used to include external libraries or modules | Python has a rich set of built-in modules and third-party libraries
import math  # Importing the math module | The math module provides access to mathematical functions
import random  # Importing the random module | The random module implements pseudo-random number generators for various distributions
import os  # Importing the os module | The os module provides a way of using operating system dependent functionality like reading or writing to the file system
import sys  # Importing the sys module | The sys module provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter
import datetime  # Importing the datetime module | The datetime module supplies classes for manipulating dates and times
# Importing the time module | The time module provides various time-related functions
import time  # Importing the time module | The time module provides various time-related functions
# Importing the json module | The json module can parse JSON from strings or files
import json  # Importing the json module | The json module can parse JSON from strings or files
# Importing the requests module | The requests module allows you to send HTTP requests using Python
import requests  # Importing the requests module | The requests module allows you to send HTTP requests using Python
# Importing the re module | The re module provides support for regular expressions
import re  # Importing the re module | The re module provides support for regular expressions
# Importing the csv module | The csv module implements classes to read and write tabular data in CSV format
import csv  # Importing the csv module | The csv module implements classes to read and write tabular data in CSV format


#Additonal Python basics include

# 11. String Manipulation | Used to manipulate strings | Strings are sequences of characters
# Strings are immutable, meaning they cannot be changed after they are created
# String concatenation | Joining two or more strings together
str1 = "Hello"
str2 = "World"
# String formatting | Inserting values into a string
formatted_str = f"{str1}, {str2}!"  # Using f-strings (Python 3.6+)
print(formatted_str)  # Output: Hello, World!
# String methods | Strings have built-in methods for manipulation
# str1.upper() | Converts the string to uppercase
# str1.lower() | Converts the string to lowercase
# str1.strip() | Removes leading and trailing whitespace
# str1.replace("o", "a") | Replaces all occurrences of "o" with "a"
# str1.split(",") | Splits the string into a list of substrings
# str1.join(["a", "b", "c"]) | Joins a list of strings into a single string

# 12. recursion | A function that calls itself
def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

# 13. List Comprehensions | A concise way to create lists | List comprehensions provide a shorter syntax when you want to create a new list based on the values of an existing list
squares = [x**2 for x in range(10)]  # List comprehension to create a list of squares
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 14. Lambda Functions | Anonymous functions | Lambda functions are small anonymous functions that can have any number of arguments but only one expression
# Lambda functions are often used for short, throwaway functions
add = lambda x, y: x + y  # Lambda function to add two numbers
print(add(5, 3))  # Output: 8   

# 15. List Slicing | Used to access a range of elements in a list | List slicing allows you to extract a portion of a list
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [2, 3, 4]  # Slicing from index 1 to 3 (4 is excluded)
print(numbers[:3])  # Output: [1, 2, 3]  # Slicing from the beginning to index 2 (3 is excluded)
print(numbers[2:])  # Output: [3, 4, 5]  # Slicing from index 2 to the end
print(numbers[-3:])  # Output: [3, 4, 5]  # Slicing from index -3 to the end
print(numbers[::2])  # Output: [1, 3, 5]  # Slicing with a step of 2

# 16. Tuples | Used to store multiple items in a single variable | Tuples are ordered and immutable | Tuples are similar to lists but cannot be changed after creation
# Tuples are written with round brackets
# Tuples can contain different data types
# Tuples can be used to store multiple items in a single variable
# Tuples are ordered, meaning the items have a defined order
# Tuples are immutable, meaning you cannot change the items after the tuple is created
# Tuples are indexed, meaning you can access the items by referring to the index number
# Tuples can be used to store multiple items in a single variable
# Tuples can be used to store different data types  

# 17. Sets | Used to store multiple items in a single variable | Sets are unordered, unchangeable, and do not allow duplicate values
# Sets are written with curly brackets
# Sets can contain different data types
# Sets are unordered, meaning the items have no defined order           
# Sets are unchangeable, meaning you cannot change the items after the set is created
# Sets do not allow duplicate values
# Sets can be used to store multiple items in a single variable
# Sets can be used to store different data types

# 18. Enumerate | Used to add a counter to an iterable | The enumerate() function adds a counter to an iterable and returns it in the form of an enumerate object
# The enumerate() function takes a collection (e.g., a list) and returns it as an enumerate object
# The enumerate object contains the index and the value of each item in the collection
# The enumerate() function is useful when you need a counter with the values in a loop
# The enumerate() function is often used with for loops     

# 19. Zip | Used to combine two or more iterables | The zip() function takes iterables (can be zero or more), makes an iterator that aggregates elements from each of the iterables, and returns it as a tuple
# The zip() function is useful when you need to combine two or more iterables into a single iterable
# The zip() function is often used with for loops
# The zip() function can be used to combine two or more lists into a single list
# The zip() function can be used to combine two or more dictionaries into a single dictionary
# The zip() function can be used to combine two or more tuples into a single tuple      

# 20. List Methods | Lists have built-in methods for manipulation
# append() | Adds an element to the end of the list
# extend() | Adds elements from another list to the end of the list         
# insert() | Adds an element at a specified position
# remove() | Removes the first occurrence of a specified element
# pop() | Removes and returns an element at a specified position
# clear() | Removes all elements from the list
# index() | Returns the index of the first occurrence of a specified element
# count() | Returns the number of occurrences of a specified element
# sort() | Sorts the list in ascending order
# reverse() | Reverses the order of the list
# copy() | Returns a shallow copy of the list
# The list() function can be used to create a list from an iterable
# The list() function can be used to create a list from a string
# The list() function can be used to create a list from a tuple
# The list() function can be used to create a list from a set
# The list() function can be used to create a list from a dictionary
# The list() function can be used to create a list from a range
# The list() function can be used to create a list from a file
# The list() function can be used to create a list from a generator
# The list() function can be used to create a list from a comprehension
# The list() function can be used to create a list from a lambda function
# The list() function can be used to create a list from a map
# The list() function can be used to create a list from a filter
# The list() function can be used to create a list from a reduce
# The list() function can be used to create a list from a zip

