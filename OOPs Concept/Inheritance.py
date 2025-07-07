# ✅ Parent class or Superclass
class A:
    def feature1(self):
        print("Feature 1 is running")

    def feature2(self):
        print("Feature 2 is running")


# ✅ Single Inheritance: Class B inherits from Class A
class B(A):  # B is a child of A
    def feature3(self):
        print("Feature 3 is running")

    def feature4(self):
        print("Feature 4 is running")


# ✅ Multilevel Inheritance: Class C inherits from B, which inherits from A
class C(B):  # C is a child of B, and grandchild of A
    def feature5(self):
        print("Feature 5 is running")


# ✅ Multiple Inheritance: Class D inherits from A and B directly
class D(A, B):  # D gets features from both A and B
    def feature6(self):
        print("Feature 6 is running")


# 🔽 Creating object of each class and accessing methods 🔽

# Object of class A → Can use only A’s features
print("\n--- Object of A ---")
a1 = A()
a1.feature1()
a1.feature2()

# Object of class B → Can use A + B features (Single Inheritance)
print("\n--- Object of B ---")
b1 = B()
b1.feature1()  # from A
b1.feature2()  # from A
b1.feature3()  # from B
b1.feature4()  # from B

# Object of class C → Can use A + B + C features (Multilevel Inheritance)
print("\n--- Object of C ---")
c1 = C()
c1.feature1()  # from A
c1.feature2()  # from A
c1.feature3()  # from B
c1.feature4()  # from B
c1.feature5()  # from C

# Object of class D → Can use A + B + D features (Multiple Inheritance)
print("\n--- Object of D ---")
d1 = D()
d1.feature1()  # from A
d1.feature2()  # from A
d1.feature3()  # from B
d1.feature4()  # from B
d1.feature6()  # from D
