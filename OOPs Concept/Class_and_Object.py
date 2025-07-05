# ---------------------------------------------------------------------
# 📘 Python OOP Concept: Class and Object
# ---------------------------------------------------------------------

# ✅ What is a Class?
# - A class is a blueprint or design in programming.
# - It defines the structure and behavior of objects.
# - It contains:
#     → Attributes (data/properties)
#     → Methods (functions that perform actions)

# 🧠 Real-life Example:
#   Class: MobilePhone
#   Attributes: brand, model, price
#   Methods: call(), send_sms(), take_photo()

# ✅ What is an Object?
# - An object is a real instance created from the class.
# - It uses the class structure but holds its own unique data.
# - You can create many objects from one class.
# - In Python, there are built-in classes (like int, str) and user-defined classes.

# 🧠 Think of it like:
#     Class = Design of a mobile phone
#     Object = Your real Samsung phone or someone else's iPhone

# ---------------------------------------------------------------------
# ✅ Now let's define a class and create objects from it
# ---------------------------------------------------------------------

# Define a class named 'MobilePhone'
class MobilePhone:
    # 🔧 __init__ method: Special method that runs when a new object is created
    # It is used to initialize the attributes of the object
    def __init__(self, brand, model, price):
        # 'self' refers to the current object
        self.brand = brand    # 📦 Store the brand of the phone
        self.model = model    # 📦 Store the model of the phone
        self.price = price    # 💰 Store the price of the phone

    # 📋 Method to display phone details
    def show_details(self):
        print(f"📱 {self.brand} {self.model} costs ₹{self.price}")

    # 📞 Method to simulate making a call
    def call(self, number):
        print(f"📞 Calling {number} from {self.brand} {self.model}...")

    # 💬 Method to simulate sending a message
    def send_sms(self, message):
        print(f"💬 Sending message: '{message}' from {self.brand} {self.model}")

# ---------------------------------------------------------------------
# ✅ Creating objects (instances) of the MobilePhone class
# ---------------------------------------------------------------------

phone1 = MobilePhone("Samsung", "Galaxy A14", 14999)   # 🔹 Object 1
phone2 = MobilePhone("Apple", "iPhone 13", 69999)      # 🔹 Object 2

# ---------------------------------------------------------------------
# ✅ Using the objects to call methods
# ---------------------------------------------------------------------

# 📲 Interacting with phone1
phone1.show_details()              # Output: Samsung Galaxy A14 costs ₹14999
MobilePhone.show_details(phone1)  # Same output, using class name and passing object
phone1.call("9876543210")         # Output: Calling 9876543210...
phone1.send_sms("Hello!")         # Output: Sending message...

print()  # ➖ Blank line for separation

# 📲 Interacting with phone2
phone2.show_details()             # Output: Apple iPhone 13 costs ₹69999
phone2.call("9999999999")         # Output: Calling 9999999999...
phone2.send_sms("Good morning!")  # Output: Sending message...
