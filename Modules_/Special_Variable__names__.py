# ✅ __name__ in Python - Full Concept Explained with Comments

# ---------------------------------------------------------------
# 🔹 What is __name__?
# ---------------------------------------------------------------
# - __name__ is a special built-in variable in Python.
# - Python sets this variable automatically in every script.
# - It tells us **how** a Python file is being used:
#   → Is the file being run directly?
#   → Or is it being imported into another file?

# ---------------------------------------------------------------
# 🔹 When you run a file directly
# ---------------------------------------------------------------
# - Example: python my_example.py
# - Then Python sets __name__ = "__main__"
# - So code inside: if __name__ == "__main__": will run

# ---------------------------------------------------------------
# 🔹 When you import a file
# ---------------------------------------------------------------
# - Example: import my_example
# - Then Python sets __name__ = "my_example"
# - So code inside: if __name__ == "__main__": will NOT run
# - This is useful when you want to reuse functions without running test code

# ---------------------------------------------------------------
# 🔹 Why use this check?
# ---------------------------------------------------------------
# - Helps you separate:
#   1. Code that should run when the file is executed directly
#   2. Code that should NOT run when the file is imported
# - Common in real-world Python programs and modules

# ---------------------------------------------------------------
# 🔹 Example Structure
# ---------------------------------------------------------------

# Define a function
def show_message():
    print("📢 Hello from show_message() function!")

# Main code block that only runs when file is executed directly
if __name__ == "__main__":
    # Since we are running this file directly, __name__ == "__main__"
    print("✅ This file is being RUN directly.")
    show_message()
else:
    # This runs only if the file is being imported
    print("📦 This file is being IMPORTED as a module.")

# ---------------------------------------------------------------
# 🔹 Summary
# ---------------------------------------------------------------
# - __name__ is "__main__" when the file is run directly
# - __name__ is "filename" when the file is imported
# - This technique is useful for:
#   → Writing test/demo code in the same file
#   → Creating reusable modules without unintended side effects
