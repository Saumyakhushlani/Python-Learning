class Computer:
    def __init__(self, name, ram):
        self.name = name
        self.ram = ram

    def update(self, ram):
        self.ram = ram

    def compare(self, other):
        return self.ram == other.ram

c1 = Computer("HP Victus", 16)
c2 = Computer("Lenovo LOQ", 16)

# All objects in Python are stored in a special area called heap memory.
# Each object gets a unique memory address which can be accessed using the id() function.
print(id(c1) == id(c2))  # Output: False, since both objects reside at different memory locations

# Every time we create an object, it gets its own memory space in the heap.

# Object size in memory depends on the number of attributes (variables) it holds.

# Who is responsible for assigning memory?
# The constructor is responsible, and in Python, the constructor is the __init__ method.

# 'Computer()' is the constructor which internally calls the __init__ method.

# Updating object properties after creation
c1.name = "MacBook Pro"

# Why is 'self' needed?
# When we call c1.update(12), it is internally interpreted as update(c1, 12)
# 'self' refers to the object that is calling the method (in this case, c1)

c1.update(12)
print(c1.name, "with RAM of", c1.ram, "GB")

# Comparing two objects
# Python doesn’t know how to compare custom objects directly, so we define our own method (compare)
if c1.compare(c2):
    print("RAM is the same for both laptops")
else:
    print("RAM is different for both laptops")

# The compare method takes two arguments:
# - the calling object (via self)
# - the object to compare with (passed explicitly)
