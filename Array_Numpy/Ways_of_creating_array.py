# ============================================
# Different Ways to Create Arrays in NumPy
# ============================================

from numpy import *

# 1️⃣ Using array()
# Converts a Python list or tuple into a NumPy array
arr1 = array([10, 20, 30, 40])
print("1. Using array():", arr1)

# 2️⃣ Using linspace(start, stop, num)
# Creates 'num' evenly spaced values between start and stop (inclusive)
#Will be divided into num parts 
#By default value of nums is 50
arr2 = linspace(1, 10, 5)
print("2. Using linspace():", arr2)
# Output: [ 1.    3.25  5.5   7.75 10.  ]

# 3️⃣ Using logspace(start, stop, num)
# Creates 'num' values between 10^start and 10^stop, spaced evenly on a log scale
arr3 = logspace(1, 3, 3)
print("3. Using logspace():", arr3)
# Output: [  10.  100. 1000.]

# 4️⃣ Using arange(start, stop, step)
# Works like Python's range(), but returns a NumPy array
arr4 = arange(1, 10, 2)
print("4. Using arange():", arr4)
# Output: [1 3 5 7 9]

# 5️⃣ Using zeros(shape)
# Creates an array filled with 0s
arr5 = zeros(5)
print("5. Using zeros():", arr5)
# Output: [0. 0. 0. 0. 0.]

# 6️⃣ Using ones(shape)
# Creates an array filled with 1s
arr6 = ones(5)
print("6. Using ones():", arr6)
# Output: [1. 1. 1. 1. 1.]

#By default values of zeroes and ones will be float to get int use zeroes(5,int)

# ✅ All arrays created above are NumPy arrays and support mathematical operations and broadcasting
