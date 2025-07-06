# In Object-Oriented Programming (OOP), we have two types of variables:
# 1. Instance Variables
# 2. Class Variables (also known as Static Variables)

class Car:
    # Class variable (shared across all instances)
    wheels = 4  # Default value common to all cars unless specifically changed

    def __init__(self, company, mil):
        # Instance variables (unique to each object)
        self.company = company  # Brand of the car
        self.mil = mil          # Mileage of the car in km/l

# Creating objects (instances of Car)
c1 = Car("BMW", 15)
c2 = Car("Audi", 18)

# Instance variables are unique for each object
print("Car 1:", c1.company, "-", c1.mil, "km/l")
print("Car 2:", c2.company, "-", c2.mil, "km/l")

# Accessing class variable
print("Wheels in Car 1:", c1.wheels)
print("Wheels in Car 2:", c2.wheels)

# Updating class variable using class name
Car.wheels = 6

# Now both instances reflect the updated class variable
print("Updated wheels in Car 1:", c1.wheels)
print("Updated wheels in Car 2:", c2.wheels)

# If we try to update wheels using an instance, it will create a new instance variable instead
c1.wheels = 8  # This creates a separate 'wheels' variable only for c1

print("After instance-level change:")
print("Car 1 wheels:", c1.wheels)  # 8 (instance variable)
print("Car 2 wheels:", c2.wheels)  # 6 (still using class variable)
print("Car class wheels:", Car.wheels)  # 6

# Summary:
# - Instance variables are defined using self and are unique to each object.
# - Class variables are shared across all instances and are defined outside __init__.
# - Changing a class variable via class name affects all objects.
# - Changing it via an object creates a separate copy for that object only.
