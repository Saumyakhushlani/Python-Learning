#There are many types of array in Python we have studied about single dimension array
# The other types are multidimensional array like 2 dimensional array and so
# Which simply means we have multiple rows and multiple columns

# In this module of array we cannot work with multidimensional array
# that's Why To work with multidimensional array we use a third party package numpy
# By default the numpy package is not available in we have to install it manually
# pip3 install numpy

from numpy import *

# Using numpy we can also handle single dimensional array
arr = array([2, 4, 6, 8], int)
print("1D NumPy array:", arr)

# Accessing elements
print("First element:", arr[0])

# Looping through the array
for i in arr:
    print("Element:", i)

# Array properties
print("Data type:", arr.dtype)
print("Shape:", arr.shape)
print("Size:", arr.size)
