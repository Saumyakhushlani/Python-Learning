# ▶️ Operator Overloading means we can redefine the behavior of operators
# (+, -, *, >, <, etc.) for our own custom classes.

# ▶️ Behind the scenes, when you write:
#     a + b
# Python actually calls:
#     a.__add__(b)
# For integers and strings, Python already has these methods implemented.
# For our own classes, we need to define them ourselves.

# ----------------------------------------------
# ✅ Quick demo with integers and strings:
a = 5
b = 6
print(a + b)          # Calls int.__add__(a, b)

s1 = "Hello"
s2 = "World"
print(s1 + s2)        # Calls str.__add__(s1, s2)

# Mixing int and str is not supported:
# print(a + s1)  # ❌ Would give TypeError

# ----------------------------------------------
# ✅ Operator Overloading Example:
# Let's create a Student class with marks m1 and m2
# and define addition (+) and comparison (>) operators.

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # 📌 Overloading the + operator
    # s1 + s2  ➡️  s1.__add__(s2)
    def __add__(self, other):
        # add marks of both students
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        # return a new Student object
        return Student(m1, m2)

    # 📌 Overloading the > operator
    # s1 > s2  ➡️  s1.__gt__(s2)
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        return r1 > r2

    # 📌 Overloading __str__ to print values instead of address
    def __str__(self):
        # must return a string
        return "{} {}".format(self.m1, self.m2)

# ----------------------------------------------
# ✅ Create objects
s1 = Student(58, 69)
s2 = Student(60, 65)

# Addition of two Student objects
s3 = s1 + s2  # calls s1.__add__(s2)
print("After addition:", s3)  # calls s3.__str__()

# Comparison of two Student objects
if s1 > s2:   # calls s1.__gt__(s2)
    print("s1 wins")
else:
    print("s2 wins")

# ----------------------------------------------
# ▶️ More Magic Methods to explore:
# __sub__  ➡️  for minus (-)
# __mul__  ➡️  for multiplication (*)
# __eq__   ➡️  for equality (==)
# __le__   ➡️  for <=
# __ge__   ➡️  for >=
# __ne__   ➡️  for !=
# And many more. Try exploring by typing `dir(int)` or `dir(str)`.

# 📌 Remember: Operator overloading is just giving special meaning
# to operators for your own classes.
# ----------------------------------------------
