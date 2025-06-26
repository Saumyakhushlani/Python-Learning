# For user input as well we have a input function 
# ===============================
# How to Take User Input in Python
# ===============================

# ✅ Basic Input
# input() function takes input from the user as a string
name = input("Enter your name: ")
print("Hello", name)

# ✅ Input as Numbers
# Convert the input to integer using int()
age = int(input("Enter your age: "))
print("You will be", age + 1, "next year.")

# ✅ Input as Float
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")

# ✅ Input Multiple Values
# Use split() to separate values, then convert if needed
x, y = input("Enter two numbers separated by space: ").split()
print("You entered:", x, "and", y)

# Convert them to integers
x, y = map(int, input("Enter two numbers again: ").split())
print("Their sum is:", x + y)

# ✅ Input a List
# User enters numbers separated by space, and we create a list
nums = list(map(int, input("Enter multiple numbers: ").split()))
print("List of numbers:", nums)


ch = input("Enter a charcter")[0]
#if we enter multiple characters the input will take all but only assign the first character to th ch

#if we want to take expression as an input and evalvate the result we can use function evalve
a=eval(input("Enter the expression"))
#If user enter 2+3-5*2
#Then the evaluated values will be stored in the a