# ===============================================
# 📌 METHOD OVERLOADING IN PYTHON (Concept & Example)
# ===============================================

# ------------------------------------------------
# ✅ NOTE:
# In languages like Java or C++, method overloading allows multiple methods
# with the same name but different parameter lists (number or type of arguments).
#
# ⚠️ BUT in Python:
# - True method overloading is NOT supported.
# - Defining a method twice with the same name will override the previous one.
# - Instead, we use:
#     ✔ Default arguments
#     ✔ *args (variable arguments)
#     ✔ **kwargs (keyword arguments)
# to achieve similar behavior.

class OverloadingExample:
    def greet(self, name=None):
        """
        This method demonstrates overloading-like behavior.
        If 'name' is given, greet personally; else, use a default greeting.
        """
        if name is not None:
            return f"Hello, {name}!"
        else:
            return "Hello, there!"

# ------------------------------------------------
# ✅ TESTING:
obj = OverloadingExample()
print(obj.greet())          # Output: Hello, there!
print(obj.greet("Alice"))   # Output: Hello, Alice!
