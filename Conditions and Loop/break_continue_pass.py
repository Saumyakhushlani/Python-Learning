# ===============================
# break, continue, and pass in Python
# ===============================

# ✅ break: used to exit the loop immediately

print("Example: break")
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at", i)
        break  # exits the loop
    print("i =", i)

# Output:
# i = 1
# i = 2
# i = 3
# i = 4
# Breaking the loop at 5

# -------------------------------

# ✅ continue: skips the current iteration and moves to the next

print("\nExample: continue")
for i in range(1, 6):
    if i == 3:
        print("Skipping", i)
        continue  # skips printing 3
    print("i =", i)

# Output:
# i = 1
# i = 2
# Skipping 3
# i = 4
# i = 5

# -------------------------------

# ✅ pass: does nothing (a placeholder for future code)

print("\nExample: pass")
for i in range(1, 4):
    if i == 2:
        pass  # placeholder; does nothing
    print("i =", i)

# Output:
# i = 1
# i = 2
# i = 3

# ✅ Summary
# break   → exits the loop
# continue → skips current iteration
# pass    → does nothing; acts as a placeholder
