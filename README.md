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

## Keywords

Keywords are reserved words in Python that have special meaning and cannot be used as identifiers (variable names, function names, etc.). They form the syntax and structure of the language. Here are some commonly used Python keywords:

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




# DataTypes

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


