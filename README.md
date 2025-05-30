# 🐍 Python Complete Revision Notes

This repository contains my personal notes and code examples while revising Python. All key concepts are listed here with concise explanations and runnable code snippets.

---

## ✅ Table of Contents

- [1. Basics](#1-basics)
- [2. Data Types](#2-data-types)
- [3. Control Flow](#3-control-flow)
- [4. Functions](#4-functions)
- [5. OOP](#5-oop)
- [6. Modules & Packages](#6-modules--packages)
- [7. File Handling](#7-file-handling)
- [8. Error Handling](#8-error-handling)
- [9. Advanced Python](#9-advanced-python)
- [10. Testing](#10-testing)

---
# 🐍 Python Overview

## 👨‍💻 Creator of Python

- **Guido van Rossum** is the creator of Python.
- He began working on Python in the late 1980s and released the first version in **1991**.
- Python was designed with readability and simplicity in mind.

---

## 📅 Python Versions Timeline

| Version      | Release Year | Notes                          |
|--------------|--------------|--------------------------------|
| Python 1.0   | 1994         | First official release         |
| Python 2.0   | 2000         | Introduced garbage collection and Unicode support |
| Python 3.0   | 2008         | Major redesign, not backward compatible |
| Latest       | *(add current version here)* | Continuously updated |

---

## 🌟 Features of Python

- ✅ **Simple and Straightforward Syntax** – easy to learn and use.
- 🔠 **Case-Sensitive** – `Variable` and `variable` are treated differently.
- 🔄 **Multi-Paradigm Language** – supports object-oriented, procedural, and functional programming styles.
- 📦 **Dynamically Typed** – no need to declare variable types explicitly.
- 👁️ **Emphasis on Code Readability** – indentation is part of the syntax.
- 🧹 **Automatic Memory Management** – garbage collection is built-in.
- 📚 **Large Standard Library** – batteries included philosophy.
- 🌍 **Huge Community Support** – lots of tutorials, packages, and help online.
- 💻 **Platform Independent** – write once, run anywhere with Python interpreters.

---

## 🛠️ What is IDLE?

- **IDLE (Integrated Development and Learning Environment)** is Python's built-in editor.
- Comes bundled with Python by default.
- Lightweight and beginner-friendly.
- Useful features:
  - Syntax highlighting
  - Code completion
  - Integrated Python shell (REPL)

To open IDLE:
- On Windows: Search for “IDLE” after installing Python.
- On macOS/Linux: Run `idle3` from the terminal (if installed).

---

# 1. Basics

## 📝 Comments

### Single-line Comments

Use the `#` symbol:

```python
# This is a single-line comment
print("Hello World")
```

### Multi-line Comments

Use triple quotes:

```python
'''
This is a
multi-line comment
'''
```

---

## 🧮 Variables

### Definition

In C/C++ you must declare variables before using them:

```c
int x = 5;
```

In Python, variable declaration and initialization happen together:

```python
x = 5  # No need to declare type
```

### Rules for Naming Variables

* Can include letters, numbers, underscores
* Must start with a letter or underscore
* Cannot start with a number
* Are **case-sensitive**

```python
valid_var = 1
Valid_Var = 2  # Different from valid_var
```

### NameError Example

```python
print(my_var)  # NameError: name 'my_var' is not defined
```

---

## 🧠 Python is Dynamically Typed

* Python allows variables to change type during execution.

```python
x = 5
x = "Hello"  # Now x is a str
```

### type() Function

```python
x = 10
print(type(x))        # <class 'int'>
print(type("Hello"))  # <class 'str'>
```

**Note:** Data types in Python are classes (e.g., `int`, `str`, etc.).
They are **not** keywords.

---

## 📦 Data Types

### Basic Data Types

* `int` – Integer numbers
* `float` – Decimal numbers
* `complex` – Complex numbers
* `bool` – Boolean (True/False)
* `str` – String/text

### Collection Data Types

* `list`
* `tuple`
* `set`
* `dict`

**Note:** There is no `char` or `double` in Python.

---

## 🧬 Memory Model in Python

### Memory Stack and Heap

* **Stack**: Manages function calls and local variables.
* **Private Heap Space**: All Python objects and data structures are stored in a heap.
* Heap is managed by Python’s memory manager.

### Objects in Heap and References

```python
x = 10  # 'x' is a reference to an integer object stored in the heap
```

* `x` is a **reference variable**
* Points to a memory block in the heap
* That memory block contains: **id, type, value**

### Garbage Collection

* When reference count of an object becomes zero, it becomes eligible for garbage collection.

---

## 📛 Namespaces

* A **namespace** is a container that maps names to objects.

### Types of Objects

* **Instance Object** – from a class
* **Function Object** – functions in memory
* **Class Object** – class definitions in memory

```python
def greet():
    pass

class Person:
    pass

x = Person()
```

Here, `greet` is a function object, `Person` is a class object, and `x` is an instance object.

> 🔹 In Python, everything is an object.

---

## 🖨️ The print() Function

Used to print output to the console.

### Parameters

* `*objects`: values to print
* `sep`: separator (default is space)
* `end`: what to print at the end (default is newline)
* `file`: file-like object (default is sys.stdout)
* `flush`: flush the output (default False)

### Examples

```python
print("Hello", "World")                      # Hello World
print("Hello", "World", sep="-")             # Hello-World
print("Hello", end="...")                    # Hello...
```

## Keywords(35 keywords)

Keywords are reserved words in Python that have special meaning and cannot be used as identifiers (variable names, function names, etc.). They form the syntax and structure of the language. Here are some commonly used Python keywords:

-**False/None/True**
-**and/as/async/await**
-**in/is/not/or**
- **if / else / elif**  
  Used for conditional branching. Executes code blocks based on conditions.

- **for / while**  
  Used for looping/repeating actions.

- **break**  
  Terminates the nearest enclosing loop.

- **continue**  
  Skips the rest of the current loop iteration and moves to the next iteration.

- **def**  
  Used to define a function.

- **return**  
  Exits a function and optionally returns a value.

- **class**  
  Used to define a class (for object-oriented programming).

- **import / from**  
  Used to import modules or specific components from modules.

- **try / except / finally**  
  Used for handling exceptions (errors) and cleaning up.

- **pass**  
  A null statement used as a placeholder where code will eventually go.

- **with**  
  Used for resource management (e.g., opening files).

- **lambda**  
  Defines an anonymous (inline) function.

- **global / nonlocal**  
  Used to declare variables’ scope.

- **assert**  
  Used for debugging to check conditions.

- **yield**  
  Used inside functions to make them generators.


This is not an exhaustive list but covers the most frequently used keywords in Python.


## ⚙️ Operators

### Types of Operators in Python

> **Note:** Python does **NOT** have increment (`++`) or decrement (`--`) operators.

1. **Arithmetic Operators**  
   Used for mathematical operations.  
   Examples: `+`, `-`, `*`, `/`, `%`, `//` (floor division), `**` (exponentiation)

2. **Comparison (Relational) Operators**  
   Used to compare values and return a Boolean result.  
   Examples: `==`, `!=`, `>`, `<`, `>=`, `<=`

3. **Logical Operators**  
   Used to combine conditional statements.  
   Examples: `and`, `or`, `not`

4. **Assignment Operators**  
   Used to assign values to variables, sometimes combined with arithmetic.  
   Examples: `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `//=` , `**=`

5. **Bitwise Operators**  
   Operate on bits of integers.  
   Examples: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift)

6. **Membership Operators**  
   Test membership in a sequence (like strings, lists, tuples).  
   Examples: `in`, `not in`

7. **Identity Operators**  
   Compare the memory locations of two objects.  
   Examples: `is`, `is not`

### 🆔 The `id()` Function

- The `id()` function returns the **unique identity** (memory address) of an object in Python.
- This identity is constant during the object’s lifetime.
- Useful to check if two variables point to the **same object**.

**Syntax:**

```python
id(object)


# 2. Data-Types


Python provides various built-in data types to store different kinds of data. Here is a brief explanation of the most commonly used ones:

- **int**  
  Represents integer numbers, both positive and negative, without a decimal point.  
  *Example:* `5`, `-10`, `1000`

- **float**  
  Represents decimal (floating-point) numbers.  
  *Example:* `3.14`, `-0.001`, `2.0`

- **str**  
  Represents a sequence of characters (text). Strings are enclosed in single, double, or triple quotes.  
  *Example:* `"Hello, World!"`, `'Python'`

- **bool**  
  Represents Boolean values, which can be either `True` or `False`. Used for logical operations and conditions.

- **list**  
  An ordered, mutable collection of items that can hold elements of different data types. Defined using square brackets.  
  *Example:* `[1, "apple", 3.14]`

- **tuple**  
  An ordered, immutable collection of items, similar to lists but cannot be changed after creation. Defined using parentheses.  
  *Example:* `(10, 20, 30)`

- **set**  
  An unordered collection of unique elements. Useful for removing duplicates and performing set operations like union and intersection. Defined using curly braces or the `set()` function.  
  *Example:* `{1, 2, 3}`

- **dict**  
  A collection of key-value pairs, where each key is unique. Useful for storing data with labels. Defined using curly braces.  
  *Example:* `{"name": "Alice", "age": 25}`


#  3. Control-Flow

Control flow statements allow us to control the execution of code blocks based on conditions or loops.

---

### ✅ Conditional Statements

Python supports the standard `if`, `elif`, and `else` for decision-making.

```python
x = 10

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

---

### 🔁 Loops

#### 1. `for` Loop

Used to iterate over a sequence (like a list, tuple, string, or range):

```python
for i in range(5):
    print(i)
```

You can also iterate over items:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

#### 2. `while` Loop

Executes a block of code as long as the condition is `True`.

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

### 🔂 Loop Control Statements

#### 🔸 `break`

Exits the loop immediately.

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

#### 🔸 `continue`

Skips the current iteration and moves to the next.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

#### 🔸 `pass`

A placeholder used when a statement is syntactically required but no action is needed.

```python
for i in range(5):
    pass  # TODO: implement later
```

---

### ❗Nested Loops

Loops within loops. Each inner loop completes all iterations before the outer loop moves to the next.

```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

---

### 🚨 `else` with Loops

`else` block runs only if the loop completes without a `break`.

```python
for i in range(3):
    print(i)
else:
    print("Loop finished without break")
```

```python
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("This will not print because loop was broken")
```

---

> ℹ️ **Note:** Python has no `do-while` loop.


# 4. Functions

Functions in Python are reusable blocks of code used to perform a specific task. They help in reducing code duplication and improving readability.

---

### ✅ Defining a Function

Use the `def` keyword:

```python
def greet(name):
    print(f"Hello, {name}!")
```

Call the function:

```python
greet("Alice")
```

---

### 🧾 Function with Return

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

---

### 🧠 Types of Arguments

- **Positional Arguments**
- **Keyword Arguments**
- **Default Arguments**
- **Variable-Length Arguments** (`*args`, `**kwargs`)

```python
def example(a, b=10):
    print(a, b)

example(5)            # Positional + default
example(a=2, b=20)    # Keyword arguments
```

---

### 🔢 *args and **kwargs

- `*args`: Accepts variable number of **positional arguments**
- `**kwargs`: Accepts variable number of **keyword arguments**

```python
def show_args(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

show_args(1, 2, 3, name="Alice", age=30)
```

---

### 💡 Lambda Functions (Anonymous Functions)

```python
square = lambda x: x * x
print(square(4))  # Output: 16
```

---

### 🧪 Built-in Functions Examples

```python
print(len("Python"))        # 6
print(sum([1, 2, 3]))        # 6
print(max(5, 10, 20))        # 20
```

---

### 🔁 Recursion

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```


# 5. OOP

Python supports object-oriented programming to model real-world entities using classes and objects.

---

### 🧬 Class and Object

A **class** is a blueprint for creating objects. An **object** is an instance of a class.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

# Creating an object
p = Person("Alice")
p.greet()  # Output: Hello, my name is Alice
```

---

### 📦 The `__init__` Method

- Called automatically when an object is created.
- Used for initializing instance variables.

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
```

---

### 📌 `self` Keyword

- Refers to the current instance of the class.
- Required as the first parameter in instance methods.

---

### 🧰 Instance Variables vs Class Variables

```python
class Car:
    wheels = 4  # Class variable

    def __init__(self, color):
        self.color = color  # Instance variable
```

---

### 🧱 Types of Methods

- **Instance Methods** – access instance data via `self`
- **Class Methods** – access class data via `cls`
- **Static Methods** – don’t access instance or class data

```python
class Demo:
    def instance_method(self):
        print("Instance Method")

    @classmethod
    def class_method(cls):
        print("Class Method")

    @staticmethod
    def static_method():
        print("Static Method")
```

---

### 🧬 Inheritance

Allows a class to inherit attributes and methods from another class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # Inherited
d.bark()   # Own method
```

---

### 🧩 Encapsulation

- Wrapping data and methods together.
- Use `_` (protected) or `__` (private) to restrict access.

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

---

### 🔁 Polymorphism

- Allows different classes to implement the same method.

```python
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Woof")

def make_sound(animal):
    animal.sound()

make_sound(Cat())
make_sound(Dog())
```

---

### 🔄 Method Overriding

- Subclass provides a new implementation of a method inherited from the parent class.

```python
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")

c = Child()
c.show()
```
# 6. Modules--Packages

---

### 📄 Module Explanation

A **module** is simply a `.py` file containing Python code (functions, variables, classes) that you can reuse in other files.

#### Example:
```python
# greetings.py
def say_hello(name):
    return f"Hello, {name}!"
```

```python
# main.py
import greetings

print(greetings.say_hello("Alice"))  # Output: Hello, Alice!
```

---

### 🗂️ Package Explanation

A **package** is a collection of modules stored in a directory with a special `__init__.py` file (can be empty). It allows for hierarchical structuring of modules.

#### Example Structure:
```
ml_package/
├── __init__.py
├── preprocessing.py
├── model.py
```

You can import like this:

```python
from ml_package import preprocessing
from ml_package.model import train_model
```

---

### 📊 Examples in ML Context

#### Modules:
- `sklearn.linear_model`
- `sklearn.metrics`
- `tensorflow.keras.layers`

#### Packages:
- `sklearn`
- `numpy`
- `pandas`
- `tensorflow`

These libraries internally organize related functionality using modules and packages.

---

### 🔌 Using `import`

#### Importing a whole module:
```python
import math
print(math.sqrt(16))
```

#### Importing specific functions:
```python
from math import sqrt
print(sqrt(16))
```

#### Aliasing:
```python
import pandas as pd
import numpy as np
```

#### Importing from your own module:
```python
from my_module import my_function
```

#### Importing from a package:
```python
from my_package.my_module import my_function
```

---

### 🔁 Module vs Package

| Feature       | Module                          | Package                             |
|---------------|----------------------------------|--------------------------------------|
| Definition    | A single `.py` file              | A folder with `__init__.py` file     |
| Structure     | Contains code, functions, etc.   | Can contain multiple modules         |
| Example       | `math`, `random`                | `sklearn`, `pandas`                  |



# 7. File-Handling

---

### 📝 Opening a File

Python uses the built-in `open()` function to work with files.

```python
file = open("example.txt", "r")  # 'r' = read mode
```

---

### 📂 File Modes

| Mode | Description               |
|------|---------------------------|
| `'r'` | Read (default)           |
| `'w'` | Write (overwrite)        |
| `'a'` | Append                   |
| `'x'` | Create (error if exists) |
| `'b'` | Binary mode              |
| `'t'` | Text mode (default)      |
| `'+'` | Read and write           |

---

### 📖 Reading from a File

```python
f = open("data.txt", "r")
content = f.read()
print(content)
f.close()
```

Other reading methods:
```python
f.readline()     # reads one line
f.readlines()    # returns list of lines
```

---

### ✍️ Writing to a File

```python
f = open("output.txt", "w")
f.write("Hello, file!")
f.close()
```

Use `'a'` to append instead of overwrite.

---

### ✅ Best Practice: Using `with`

```python
with open("file.txt", "r") as f:
    data = f.read()
    print(data)
# No need to call f.close() – it's automatic
```

---

### 📜 Writing List of Lines

```python
lines = ["Line 1\n", "Line 2\n"]
with open("notes.txt", "w") as f:
    f.writelines(lines)
```

---

### 🔄 Reading & Writing Files Together

```python
with open("file.txt", "r+") as f:
    print(f.read())       # Read
    f.write("\nNew line") # Write
```

---

### ⚠️ Common Errors

- **FileNotFoundError** – Trying to read a non-existent file.
- **PermissionError** – No write permission.
- **ValueError** – Invalid mode.

---

### 📌 Tips

- Always close the file or use `with` statement.
- Prefer `with` block for safe file handling.
- Use `'rb'`, `'wb'` for binary files (e.g., images, audio).


# 8. Error-Handling

---

### 🔍 What is Error Handling?

Error handling allows your program to respond to runtime errors gracefully without crashing.

---

### ⚠️ Types of Errors

- **SyntaxError** — Mistakes in code syntax.
- **NameError** — Using undefined variables.
- **TypeError** — Invalid operations between incompatible types.
- **ValueError** — Passing wrong values to functions.
- **IndexError** — Accessing invalid list index.
- **KeyError** — Accessing non-existent dictionary key.
- **ZeroDivisionError** — Division by zero.

---

### 🔧 Try-Except Block

Catches and handles exceptions.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

---

### 🧹 Finally Block

Runs code regardless of exceptions, often for cleanup.

```python
try:
    f = open("file.txt")
    # do something
except FileNotFoundError:
    print("File not found!")
finally:
    f.close()
```

---

### 🐞 Else Block

Executes if no exceptions occur in the `try` block.

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"You entered: {num}")
```

---

### 🎯 Raising Exceptions

You can manually raise exceptions using `raise`.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
```

---

### 📋 Custom Exceptions

Define your own exception classes by inheriting from `Exception`.

```python
class CustomError(Exception):
    pass

raise CustomError("This is a custom error")
```

---

### 🧩 Common Exception Handling Tips

- Catch specific exceptions, not general ones.
- Use multiple except blocks for different errors.
- Avoid bare `except:` without specifying error type.
- Clean up resources in `finally` or use context managers (`with`).


