# ========================================================
# Variable Scope in Python: Local, Global, global & nonlocal
# ========================================================

# 🔹 GLOBAL VARIABLE
x = 100  # This is a global variable (outside any function)

def print_global():
    print("Inside function (access global x):", x)

print("1. Global Variable Access:")
print_global()
print("Outside function (x):", x)

# --------------------------------------------------------

# 🔹 LOCAL VARIABLE
def local_example():
    y = 50  # local to this function only
    print("\n2. Local Variable inside function:", y)

local_example()
# print(y)  #  Error: y is not defined outside

# --------------------------------------------------------

# 🔹 MODIFICATION of global variable inside function (❌ without global)
a = 10

def try_modify():
    a = a + 5  # Error without global keyword
    print("\nTrying to modify a:", a)

# try_modify()  # ❌ Uncomment to see UnboundLocalError

# --------------------------------------------------------

# 🔹 USING global keyword
b = 20

def modify_global():
    global b
    b = b + 10
    print("\n3. Modified global b inside function:", b)

print("\nBefore modifying b:", b)
modify_global()
print("After modifying b:", b)

# ============================
# global keyword and globals()
# ============================

# This is a global variable
x = 10

# Example 1: Using global keyword
def update_x():
    global x  # Tells Python to use the global x
    print("Before changing x (inside function):", x)
    x = x + 5  # Change the global variable
    print("After changing x (inside function):", x)

print("1. global keyword example:")
print("Before function call, x =", x)
update_x()
print("After function call, x =", x)


# ----------------------------

# Another global variable
y = 100

# Example 2: Using globals() function
def update_y():
    print("\nBefore changing y using globals():", globals()['y'])
    globals()['y'] = 200  # Update y using globals dictionary
    print("After changing y using globals():", globals()['y'])

print("\n2. globals() function example:")
print("Before function call, y =", y)
update_y()
print("After function call, y =", y)

# ----------------------------

# Example 3: Creating new global variable using globals()
def create_new():
    globals()['new_var'] = "Hello, I am global!"

create_new()
print("\n3. Creating a new global variable using globals():")
print("new_var =", new_var)
