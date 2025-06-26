# To use math inbuilt functions, we first need to import the math library
import math

# -----------------------------
# Square root
# -----------------------------
# To find the square root of a number
x = math.sqrt(28)
print("Square root of 28 is:", x)
# Output: float value (approximately 5.2915)

# -----------------------------
# Floor
# -----------------------------
# The floor function returns the largest integer less than or equal to the given number
print("Floor of 2.9 is:", math.floor(2.9))
# Output: 2

# -----------------------------
# Ceil (Ceiling)
# -----------------------------
# The ceil function returns the smallest integer greater than or equal to the given number
print("Ceil of 2.1 is:", math.ceil(2.1))
# Output: 3

# -----------------------------
# Power
# -----------------------------
# Power function returns x raised to the power y
print("3 raised to the power 2 is:", math.pow(3, 2))
# Output: 9.0 (note: always returns float)
# It's better to use math.pow(x, y) for clarity, especially when working with math functions

# -----------------------------
# Factorial
# -----------------------------
# Factorial of an integer n (n!) is the product of all integers from 1 to n
print("Factorial of 5 is:", math.factorial(5))
# Output: 120

# -----------------------------
# Trigonometric functions
# -----------------------------
# The math library provides several trigonometric functions like sin, cos, tan
# Note: The input should be in radians

angle_degrees = 90
angle_radians = math.radians(angle_degrees)  # Convert degrees to radians

print("Sine of 90 degrees:", math.sin(angle_radians))
print("Cosine of 90 degrees:", math.cos(angle_radians))
print("Tangent of 90 degrees:", math.tan(angle_radians))

# -----------------------------
# Mathematical constants
# -----------------------------
# The math library provides commonly used constants

print("Value of Pi:", math.pi)
# Output: 3.141592653589793

print("Value of Euler's number (e):", math.e)
# Output: 2.718281828459045

# -----------------------------
# Logarithmic functions
# -----------------------------
# Natural logarithm (base e)
print("Natural log of 10 is:", math.log(10))

# Logarithm with base 10
print("Base-10 log of 1000 is:", math.log10(1000))

# -----------------------------
# Degrees and Radians conversion
# -----------------------------
# Convert degrees to radians
print("180 degrees in radians is:", math.radians(180))

# Convert radians to degrees
print("π radians in degrees is:", math.degrees(math.pi))

# -----------------------------
# GCD (Greatest Common Divisor)
# -----------------------------
print("GCD of 48 and 64 is:", math.gcd(48, 64))
# Output: 16


# --------------------------------
# Importing math with an alias
# --------------------------------
import math as m

# Now you can use 'm' instead of 'math'
print("Square root of 16 is:", m.sqrt(16))
print("Floor of 3.7 is:", m.floor(3.7))
print("Value of Pi:", m.pi)

#If we don't want to import everything from math 
from math import sqrt,pow
#now we can use them without using math. we can directly use them 