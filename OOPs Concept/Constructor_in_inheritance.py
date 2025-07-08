# ✅ Parent class A
class A:
    def __init__(self):
        print("In A __init__")  # Constructor of class A

    def feature1(self):
        print("Feature 1 is running")

    def feature2(self):
        print("Feature 2 is running")


# ✅ Class B inherits from A
class B(A):
    def __init__(self):
        print("In B __init__")  # Constructor of class B
        super().__init__()      # Calls constructor of A

    def feature3(self):
        print("Feature 3 is running")

    def feature4(self):
        print("Feature 4 is running")


# 👉 Creating object of class B
print("\n--- Creating object of class B ---")
b1 = B()

# ✅ Since B has its own __init__, it runs first.
# ✅ Inside B's __init__, we explicitly call A's __init__ using super().__init__()


# ✅ Class C inheriting from both A and B
class C(A, B):
    def __init__(self):
        print("In C __init__")
        super().__init__()  # Calls next class's __init__ in MRO


# 👉 Creating object of class C
print("\n--- Creating object of class C ---")
c1 = C()

# ✅ MRO decides which class's __init__ is called by super()
# ✅ Since C inherits from (A, B), the order is: C → A → B
# ✅ So super().__init__() in C calls A's __init__, NOT B's


# ✅ We can print the MRO of class C using __mro__ or mro()
print("\n--- Method Resolution Order (MRO) of class C ---")
print(C.__mro__)  # tuple showing MRO
# or
print(C.mro())    # list showing MRO

# We can use super meathord also to call the methods of superclass in subclass