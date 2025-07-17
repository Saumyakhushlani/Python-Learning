# ===============================================
# 📌 METHOD OVERRIDING IN PYTHON (Concept & Example)
# ===============================================

# ------------------------------------------------
# ✅ NOTE:
# Method overriding occurs in inheritance when a subclass
# provides a specific implementation of a method that is already defined in its parent class.
#
# 🔹 Parent class has a method
# 🔹 Child class defines the SAME method name
# 🔹 The child's method OVERRIDES the parent's method when called from the child instance.

class Parent:
    def show(self):
        """Parent class method"""
        return "This is Parent's show() method"

class Child(Parent):
    def show(self):
        """Child overrides the parent's show method"""
        return "This is Child's show() method (overridden)"

# ------------------------------------------------
# ✅ TESTING:
p = Parent()
print(p.show())   # Output: This is Parent's show() method

c = Child()
print(c.show())   # Output: This is Child's show() method (overridden)
