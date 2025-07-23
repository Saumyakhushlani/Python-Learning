# Let's say we have two variables:
a = 5
b = 6
print("Initially: a =", a, "b =", b)

# -------------------------------------------------
# 🟡 METHOD 1: Using a third variable (common in many languages)
temp = a        # store 'a' in temp
a = b           # assign b to a
b = temp        # assign temp to b
print("After swap using third variable: a =", a, "b =", b)

# reset values
a, b = 5, 6

# -------------------------------------------------
# 🟡 METHOD 2: Using + and - (without third variable)
# a = a + b
# b = a - b
# a = a - b
a = a + b
b = a - b
a = a - b
print("After swap using + and - : a =", a, "b =", b)

# reset values
a, b = 5, 6

# -------------------------------------------------
# 🟡 METHOD 3: Using XOR (bitwise ^ operator)
# This does not use extra bits beyond what is needed
a = a ^ b
b = a ^ b
a = a ^ b
print("After swap using XOR: a =", a, "b =", b)

# reset values
a, b = 5, 6

# -------------------------------------------------
# 🟡 METHOD 4: Pythonic way (tuple unpacking)
# This is unique to Python and very simple
a, b = b, a
print("After swap using Python tuple unpacking: a =", a, "b =", b)

# -------------------------------------------------
# ✅ Summary:
# Method 1: temp variable
# Method 2: + and -
# Method 3: XOR
# Method 4: Python tuple unpacking (most recommended in Python)
