# ===============================
# if, elif, else, and nested if
# ===============================

# ✅ Basic if statement
num = int(input("Enter a number: "))

# To right multiple statements in if the spacing before the statement are same

if (num > 0):
    print("The number is positive")
    print("Yhats to toadd multiple statements")

# ✅ if...else statement
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# ✅ if...elif...else ladder
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F (Fail)")

# ✅ Nested if example
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
    if age >= 60:
        print("You are also a senior citizen")
    else:
        print("You are not a senior citizen")
else:
    print("You are a minor")

# ✅ Another nested if example
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Unknown user")
