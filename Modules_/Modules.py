# When programs grow big, they become harder to manage in a single file.
# Imagine writing all your functions, classes, and logic in one long file – it becomes messy and hard to debug.
# To keep the code clean, **organized**, and **reusable**, Python lets you divide it into separate files called "modules".
# This way, you can write once and use it in many projects by importing the module.

# A module is simply a **Python file (.py)** that contains definitions of functions, classes, or variables.
# For example, if you create a file `math_tools.py` with a function inside it, that file becomes a module.

# Example:  math_tools.py
# def add(a, b):
#     return a + b

# You can now use it in another file:
# from math_tools import add
# print(add(2, 3))  # Output: 5
