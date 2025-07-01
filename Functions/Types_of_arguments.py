# ===============================================
# Types of Arguments in Python
# 1. Formal and Actual Arguments
# 2. Default Arguments
# ===============================================

# 🔹 Function definition (Formal Arguments: name, city)
def introduce(name, city):
    print("Hello,", name)
    print("You are from", city)

# 🔸 Function call (Actual Arguments: "Saumya", "Bhopal")
print("1. Formal and Actual Arguments:")
introduce("Saumya", "Bhopal")
# Output:
# Hello, Saumya
# You are from Bhopal


# -----------------------------------------------

# 🔹 Function with a Default Argument
def greet(name, age=18):  # age has a default value
    print(f"\nHi {name}, your age is {age}")

print("\n2. Default Argument Examples:")

# 🔸 Case 1: Only name passed, default age is used
greet("Ravi")
# Output: Hi Ravi, your age is 18

# 🔸 Case 2: Both name and age passed, default is overridden
greet("Aman", 21)
# Output: Hi Aman, your age is 21


# ===============================================
# Types of Actual Arguments in Python
# 1. Positional
# 2. Keyword
# 3. Default
# 4. Variable-Length (*args, **kwargs)
# ===============================================

# 🔹 Function definition for examples
def student_info(name, age=18, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

# 1️⃣ Positional Arguments → values assigned based on position
print("1. Positional Arguments:")
student_info("Ravi", 21, "Delhi")
# Output: Name: Ravi, Age: 21, City: Delhi

# 2️⃣ Keyword Arguments → specify argument name during call
print("\n2. Keyword Arguments:")
student_info(age=22, name="Aman", city="Mumbai")
# Output: Name: Aman, Age: 22, City: Mumbai

# 3️⃣ Default Arguments → use defaults when value not passed
print("\n3. Default Arguments:")
student_info("Neha")  # age=18 and city='Unknown' will be used
# Output: Name: Neha, Age: 18, City: Unknown

# 4️⃣ Variable-Length Arguments
# 🔸 *args → collects extra positional arguments as tuple
# 🔸 **kwargs → collects extra keyword arguments as dictionary

def show_scores(*scores):
    print("\n4.1 Variable-Length Positional (*args):")
    print("Scores:", scores)

show_scores(85, 90, 75)
# Output: Scores: (85, 90, 75)

def show_profile(**details):
    print("\n4.2 Variable-Length Keyword (**kwargs):")
    for key, value in details.items():
        print(f"{key} = {value}")

show_profile(name="Saumya", branch="CSE", year=2)
# Output:
# name = Saumya
# branch = CSE
# year = 2

