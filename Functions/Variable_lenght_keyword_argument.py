# ==================================================
# Variable-Length Keyword Arguments in Python (**kwargs)
# ==================================================

# ✅ What is **kwargs?
# It allows you to pass any number of keyword arguments to a function.
# These arguments are captured as a dictionary inside the function.

# 🔹 Function using **kwargs
def show_details(**kwargs):
    print("Received details:")
    for key, value in kwargs.items():
        print("{key} = {value}")

# 🔸 Function calls with different keyword arguments
print("Example 1:")
show_details(name="Saumya", age=20, branch="CSE")

print("\nExample 2:")
show_details(subject="Math", marks=95, passed=True)

# ----------------------------------------------

# ✅ Combining normal and **kwargs
def introduce(role, **kwargs):
    print(f"\nHello! You are a {role}.")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\nExample 3 (with fixed and variable arguments):")
introduce("Student", name="Aman", year=2, city="Delhi")

# ----------------------------------------------

# ✅ Passing a dictionary using ** operator
info = {
    "name": "Priya",
    "course": "Python",
    "duration": "2 months"
}

print("\nExample 4 (unpacking dictionary):")
show_details(**info)

# ----------------------------------------------

# ✅ Summary:
# - Use `**kwargs` when you want a function to accept any number of keyword arguments.
# - Inside the function, kwargs is a dictionary.
# - Useful when designing flexible APIs or functions.

