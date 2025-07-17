x = 5
x = 'Navin'

# ✅ Duck Typing Concept:
# The moment we give a variable name (like x), it's just a *name* to the memory.
# Python uses **dynamic typing**, so x can refer to different types at different times.
# When x = 5 → memory stores an int object; x is just a label.
# When x = 'Navin' → memory now stores a str object; x still just a label.

# ✅ Define a class that has a method named 'execute'
class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

# ✅ Another class which *expects* an object that has an 'execute' method
class Laptop:
    def code(self, ide):  # We don't care about ide's class, just that it has an execute() method
        ide.execute()

# ✅ Create an instance of PyCharm and pass it to Laptop's code method
ide = PyCharm()
lap1 = Laptop()
lap1.code(ide)

# ✅ Important Duck Typing Concept:
# The type of 'ide' here is PyCharm, but is it fixed? ❌ No!
# We can pass any object to 'code()' as long as it has an 'execute()' method.
# This is called **duck typing**:
# “If it walks like a duck, quacks like a duck, and swims like a duck — it’s a duck.”
# So in Python, we don’t care about the object's type — only its behavior matters.
