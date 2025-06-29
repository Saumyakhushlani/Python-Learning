# ============================================
# Introduction to Arrays in Python (array module)
# ============================================

# Array basically means a list with values of the same data type.
# The values should be of the same type (all integers, all floats, etc.)
# Python arrays can grow and shrink (unlike C/C++ fixed-size arrays).

# ✅ To use array, we must import the array module
# Method 1:
# import array as arr

# Method 2 (Recommended for beginners):
from array import *

# ✅ Creating an array
# Syntax: array(typecode, [elements])

# Typecodes:
# 'i' → signed int
# 'f' → float
# 'u' → Unicode character
# 'd' → double
# 'b' → signed char
# 'l' → signed long

# Example: Create an array of integers
vals = array('i', [10, 20, 30, 40])
print("Original array:", vals)

# ✅ Accessing elements
print("First element:", vals[0])
print("Last element:", vals[-1])

# ✅ Loop through array using for loop
print("All elements:")
for val in vals:
    print(val)

# ✅ Using index while looping
print("Elements with index:")
#len(vals)
for i in range(len(vals)):
    print("Index {i}: Value {vals[i]}")

# ✅ Adding elements
vals.append(50)
print("After append:", vals)

# ✅ Inserting element at specific position
vals.insert(2, 25)  # insert 25 at index 2
print("After insert:", vals)

# ✅ Removing elements
vals.remove(20)  # removes first occurrence of 20
print("After removing 20:", vals)

# ✅ Pop last element
vals.pop()
print("After pop:", vals)

# ✅ Reverse the array
vals.reverse()
print("After reverse:", vals)

# ✅ Array buffer info (memory address and size)
print("Buffer info:", vals.buffer_info())

# ✅ Count occurrences
vals.append(10)
print("10 occurs", vals.count(10), "times")

#vals.typecode returns the type of array like signed integer etc.

# ✅ Copying array
newArr = array(vals.typecode, (a for a in vals))
print("Copied array:", newArr)

# ✅ Creating array from user input (optional)
n = int(input("\nHow many elements do you want to add? "))
user_arr = array('i', [])

for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    user_arr.append(x)

print("User entered array:", user_arr)

#Inbuild Function to find the index of a value
vals.index(10)