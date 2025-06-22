# Python: Variables, Strings, and Lists

# ---- Underscore in Python REPL ----
# In the Python interactive shell, the underscore (_) stores the result of the last expression.
# Example:
# >>> 3 + 2
# 5
# >>> _
# 5

# ---- Integer Division ----
# Integer division in Python is done using //
result = 3 // 2  # result will be 1

# ---- Strings ----
name = "Saumya"

# Indexing
print(name[0])   # 'S'
print(name[-1])  # 'a'

# Slicing
print(name[0:2])     # 'Sa' (includes index 0, excludes 2)
print(name[0:100])   # Prints entire string without error
print(name[0:])      # Prints entire string from index 0

# Strings are immutable
# name[0] = "R"  # This will throw an error

# But we can create a new string
new_name = "R" + name[1:]  # 'Raumya'

# Length of a string
length = len(name)  # 6

# ---- Lists ----
# Lists can hold multiple values (like arrays)
nums = [25, 16, 4, 8, 12]
print(nums[0])  # 25
print(nums[4])  # 12

# List slicing
print(nums[3:])     # [8, 12]
print(nums[0:2])    # [25, 16]

# Negative indexing
print(nums[-1])     # 12

# List of strings
names = ["navin", "saumya", "john"]

# Mixed data type list
values = [9.5, "Navin", 25]

# List of lists
mis = [names, values, nums]

# Lists are mutable
nums[0] = 100  # This is allowed

# Common list functions
nums.append(50)      # Adds 50 to the end
nums.insert(2, 33)   # Inserts 33 at index 2
nums.remove(4)       # Removes the value 4
nums.pop()           # Removes the last element
nums.pop(1)          # Removes the element at index 1
nums.sort()          # Sorts the list
nums.reverse()       # Reverses the list
nums.clear()         # Removes all elements from the list
del nums[2:]         # Delete multiple elemets at the same time
nums.extend[(29,12,14)]  #Add multiple values at the same time

#----------- Inbuild Functions in Python for lists ----------
min(nums)            #Return the minimum value in a list
max(nums)            #Return the maximum value in a list
sum(nums)            #Return the sum of all the value in a list
len(nums)            #Return the lenght of the lists


# Print modified list
print(nums)
