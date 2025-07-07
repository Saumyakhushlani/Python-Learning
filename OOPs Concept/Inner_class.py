# Outer class representing a student
class Student:
    def __init__(self, name, roll):
        # Initializing student name and roll number
        self.name = name
        self.roll = roll
        # Creating an object of the inner Laptop class for each student
        self.laptop = self.Laptop()

    def details(self):
        # Printing student details
        print(f"Name: {self.name}, Roll no: {self.roll}")
        # Calling the details method of the Laptop object
        self.laptop.details()

    # Inner class representing a laptop (specific to each student)
    class Laptop:

        def __init__(self):
            # Initializing default laptop specifications
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = 16

        def details(self):
            # Printing laptop details
            print(self.brand, self.cpu, self.ram)

# Creating a Student object
s1 = Student("Saumya", 55)

# Calling the details method of Student, which also prints Laptop details
s1.details()

# Accessing the brand attribute of the student's laptop directly
s1.laptop.brand

# OR: storing the laptop object in a variable and then accessing its attributes
lap1 = s1.laptop
lap1.brand

# OR: creating a separate Laptop object manually
lap1 = Student.Laptop()
