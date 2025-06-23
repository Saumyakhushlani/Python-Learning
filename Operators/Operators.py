# ---- Arithmetic Operators ---------
# These are used to perform mathematical operations
a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)         # 13
print("Subtraction:", a - b)      # 7
print("Multiplication:", a * b)   # 30
print("Division:", a / b)         # 3.333...
print("Floor Division:", a // b)  # 3 (discards decimal)
print("Modulus:", a % b)          # 1 (remainder)
print("Exponent:", a ** b)        # 1000 (10^3)
print()

# ---- Assignment Operators ---------
# Used to assign values to variables and modify them
x = 5
#Assignment of more variables can be also done in one line itself
a,b=2,3

print("Assignment Operators:")
x += 3  # same as x = x + 3
print("x += 3:", x)

x -= 2  # x = x - 2
print("x -= 2:", x)

x *= 4  # x = x * 4
print("x *= 4:", x)

x /= 3  # x = x / 3
print("x /= 3:", x)

x %= 2  # x = x % 2
print("x %= 2:", x)

x **= 3  # x = x ** 3
print("x **= 3:", x)

x //= 2  # x = x // 2
print("x //= 2:", x)
print()

# ---- Relational Operators (Comparison Operators) ---------
# Used to compare two values, returns True or False
a = 10
b = 20
print("Relational Operators:")
print("a == b:", a == b)    # False
print("a != b:", a != b)    # True
print("a > b:", a > b)      # False
print("a < b:", a < b)      # True
print("a >= b:", a >= b)    # False
print("a <= b:", a <= b)    # True
print()

# ---- Logical Operators ---------
# Used to combine conditional statements
x = True
y = False
print("Logical Operators:")
print("x and y:", x and y)  # False
print("x or y:", x or y)    # True
print("not x:", not x)      # False
print()

# ---- Unary Operators ---------
# Operators with only one operand, such as negation
n = 5
print("Unary Operators:")
print("Original value of n:", n)
print("Unary negation -n:", -n)  # -5 (makes positive number negative)
