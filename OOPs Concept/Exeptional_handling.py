# errors_and_exceptions.py
# ------------------------------------------------------
# Types of Errors in Python
# ------------------------------------------------------
# 1️⃣ Compile-time Errors (Syntax Errors):
#    → Mistakes in syntax (missing colon, wrong indentation, misspelling `print`)
#    → Detected before running the program.
#
# 2️⃣ Logical Errors:
#    → Code runs but output is wrong due to wrong logic.
#    → Example: expecting 2+3 = 5 but code returns 4.
#
# 3️⃣ Runtime Errors:
#    → Code compiles and logic is correct, but error happens while running.
#    → Example: dividing by zero, file not found, network failure.
#    → Must be handled gracefully.

# ------------------------------------------------------
# Handling runtime errors using try–except–finally
# ------------------------------------------------------

# Simulating a critical operation
a = 5
b = 0   # change to 2 later to see normal flow

try:
    print("Resource opened (e.g. file or DB connection).")
    # critical operation
    result = a / b
    print("Result is:", result)

# Specific exception for division by zero
except ZeroDivisionError as e:
    print("❌ You cannot divide a number by zero.")
    print("Error detail:", e)

# You can add more except blocks for specific errors
except ValueError as e:
    print("❌ Invalid value provided by user.")
    print("Error detail:", e)

# Generic exception (catch-all)
except Exception as e:
    print("⚠️ Something went wrong:", e)

# finally block always runs
finally:
    print("Resource closed (e.g. file/DB connection cleanup).")

# ------------------------------------------------------
# Example of taking input and handling it
# ------------------------------------------------------

try:
    x = int(input("Enter a number: "))  # may raise ValueError
    y = int(input("Enter another number: "))  # may raise ValueError
    print("Division result:", x / y)

except ZeroDivisionError:
    print("❌ Cannot divide by zero.")
except ValueError:
    print("❌ Please enter only numbers.")
except Exception as e:
    print("⚠️ Unexpected error:", e)
finally:
    print("✅ Clean up done, program continues...")

# ------------------------------------------------------
# Quick recap:
# ✅ try: put your critical statements here
# ✅ except: handle specific or generic errors
# ✅ finally: cleanup code that must run no matter what
# ------------------------------------------------------
