# ✅ What is a Class?

# - A class is a blueprint or design in programming.
# - It defines the structure and behavior of objects.
# - It contains:
#     → Attributes (data/properties)
#     → Methods (functions that perform actions)

# 🧠 Example in real life:
#   Class: MobilePhone
#   Attributes: brand, model, price
#   Methods: call(), send_sms(), take_photo()

# ---------------------------------------------------------------------

# ✅ What is an Object?

# - An object is a real instance created from the class.
# - It uses the class structure but holds its own unique data.
# - You can create many objects from one class. 
# - In Python there are some inbuilt class like integer string and we can also create our own classes


# 🧠 Think:
#     Class = Design of a mobile phone
#     Object = Your real Samsung phone or someone else's iPhone

# ---------------------------------------------------------------------
# ✅ Now let's write a class and create objects from it
# ---------------------------------------------------------------------

# Define a class named 'MobilePhone'
class MobilePhone:
    # Constructor method to initialize data when object is created
    def __init__(self, brand, model, price):
        self.brand = brand    # Attribute: phone brand
        self.model = model    # Attribute: phone model
        self.price = price    # Attribute: phone price

    # Method to display the phone's details
    def show_details(self):
        print(f"📱 {self.brand} {self.model} costs ₹{self.price}")

    # Method to simulate making a call
    def call(self, number):
        print(f"📞 Calling {number} from {self.brand} {self.model}...")

    # Method to simulate sending a message
    def send_sms(self, message):
        print(f"💬 Sending message: '{message}' from {self.brand} {self.model}")

# ---------------------------------------------------------------------
# ✅ Creating objects (instances) of the class
# ---------------------------------------------------------------------

phone1 = MobilePhone("Samsung", "Galaxy A14", 14999)   # Object 1
phone2 = MobilePhone("Apple", "iPhone 13", 69999)      # Object 2

# ---------------------------------------------------------------------
# ✅ Using the objects to call methods
# ---------------------------------------------------------------------

# For phone1
# If we want to use a meathord first we have to mention objectname then call the function
phone1.show_details()         # Output: Samsung Galaxy A14 costs ₹14999
phone1.call("9876543210")     # Output: Calling 9876543210...
phone1.send_sms("Hello!")     # Output: Sending message...

print()  # Blank line for separation

# For phone2
phone2.show_details()         # Output: Apple iPhone 13 costs ₹69999
phone2.call("9999999999")     # Output: Calling 9999999999...
phone2.send_sms("Good morning!")  # Output: Sending message...
