# In Python, we have three types of methods in OOP:
# 1. Instance Method
# 2. Class Method
# 3. Static Method

class Student:

    # Class variable shared across all instances
    school = "Telusko"

    def __init__(self, m1, m2, m3):
        # Instance variables unique to each object
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance Method
    def avg(self):
        # Accessor method (used to fetch/access data)
        return (self.m1 + self.m2 + self.m3) / 3

    # Mutator method (used to modify instance data)
    def update_marks(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Class Method
    @classmethod
    def get_school(cls):
        # 'cls' refers to the class itself
        return cls.school

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # Static Method
    @staticmethod
    def info():
        # Does not access class or instance variables
        print("This is the Student class. It stores marks and school name.")


# Creating objects
s1 = Student(24, 67, 89)
s2 = Student(56, 78, 90)

# Calling instance method (avg)
print("Average marks of s1:", s1.avg())
print("Average marks of s2:", s2.avg())

# Updating marks using mutator method
s1.update_marks(90, 91, 92)
print("Updated average marks of s1:", s1.avg())

# Accessing class method
print("School name (via class method):", Student.get_school())

# Changing class variable using class method
Student.change_school("CodeWithHarry")
print("Updated school name:", s1.get_school())

# Calling static method
Student.info()
