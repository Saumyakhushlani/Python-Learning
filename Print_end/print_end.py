# ============================
# Understanding print(..., end=...)
# ============================

# By default, print() adds a newline (\n) after printing
print("This is line 1")
print("This is line 2")

# Output:
# This is line 1
# This is line 2

# -----------------------------
# Using end=" " (space)
# -----------------------------
# This prints on the same line with a space between them
print("Hello", end=" ")
print("World")

# Output:
# Hello World

# -----------------------------
# Using end="" (no space, no newline)
# -----------------------------
print("Python", end="")
print("Rocks")

# Output:
# PythonRocks

# -----------------------------
# Using end with custom characters
# -----------------------------
print("Loading", end="...")
print("Done")

# Output:
# Loading...Done

# -----------------------------
# Printing numbers in a loop on the same line
# -----------------------------
for i in range(1, 6):
    print(i, end=" ")  # print numbers with a space
print()  # just to add a newline after the loop ends

# Output:
# 1 2 3 4 5

# -----------------------------
# Using end to create patterns
# -----------------------------
for i in range(5):
    print("*", end="")  # no space or newline
print()  # move to next line after printing *****

# Output:
# *****

# -----------------------------
# Summary
# -----------------------------
# - end="\n" is the default → prints in new line
# - end=" " → prints in the same line with space
# - end="" → prints in the same line with no space
# - end="..." or any string → adds custom characters at the end
