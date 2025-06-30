# ============================================
# Basic Operations on NumPy Arrays
# ============================================

from numpy import *

# ✅ Create a simple 1D NumPy array
arr = array([1, 2, 3, 4, 5])
print("Original array:", arr)

# ============================================
# 🔹 Adding 5 to all elements
# NumPy allows vectorized operations — fast and easy
new_arr = arr + 5
print("After adding 5 to each element:", new_arr)

# This works element-wise:
# [1+5, 2+5, 3+5, 4+5, 5+5] → [6 7 8 9 10]

# ============================================
# 🔹 Multiply all elements by 2
multiplied_arr = arr * 2
print("After multiplying each element by 2:", multiplied_arr)

# ============================================
# 🔹 Element-wise comparison
print("Is arr > 3:", arr > 3)
# Output: [False False False  True  True]





# ✅ Create two arrays
arr1 = array([10, 20, 30, 40])
arr2 = array([1, 2, 3, 4])
print("Array 1:", arr1)
print("Array 2:", arr2)

# ==============================================
# 🔹 1. Adding two arrays (element-wise)
added = arr1 + arr2
print("\n1. Element-wise Addition:", added)
# Output: [11 22 33 44]

# ==============================================
# 🔹 2. Sine of array elements
# NumPy trigonometric functions work in radians
sin_arr = sin(arr1)
print("\n2. Sine of Array 1 (radians):", sin_arr)

# ==============================================
# 🔹 3. Sum of array elements
total_sum = sum(arr1)
print("\n3. Sum of Array 1:", total_sum)

# ==============================================
# 🔹 4. Sorting an array
unsorted = array([5, 1, 9, 3])
sorted_arr = sort(unsorted)
print("\n4. Sorted Array:", sorted_arr)

# ==============================================
# 🔹 5. Concatenating arrays
concat_arr = concatenate([arr1, arr2])
print("\n5. Concatenated Array:", concat_arr)

# ==============================================
# 🔹 6. Copying Arrays — Reference vs Copy

# Reference assignment (both variables point to the same array)
arr3 = arr1
arr3[0] = 100
print("\n6. Reference Copy (arr3 = arr1):")
print("arr1:", arr1)
print("arr3:", arr3)
print("Same address:", id(arr1) == id(arr3))  # True

# Deep copy (independent copy with different address)
arr4 = arr1.copy()
arr4[1] = 200
print("\nActual Copy using .copy():")
print("arr1:", arr1)
print("arr4:", arr4)
print("Different address:", id(arr1) != id(arr4))  # True
