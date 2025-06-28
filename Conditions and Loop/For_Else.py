# ===============================
# for...else in Python
# ===============================

# ✅ Basic for...else example
print("Example 1: Basic for...else")

for i in range(5):
    print("i =", i)
else:
    print("Loop finished normally!")

# Output:
# i = 0
# i = 1
# i = 2
# i = 3
# i = 4
# Loop finished normally!

# -------------------------------

# ✅ for...else with break
print("\nExample 2: for...else with break")

for i in range(5):
    print("i =", i)
    if i == 2:
        print("Breaking at", i)
        break
else:
    print("Loop completed without break")

# Output:
# i = 0
# i = 1
# i = 2
# Breaking at 2

# (Note: else block is skipped because of break)

# -------------------------------

# ✅ Searching example using for...else
print("\nExample 3: Searching in a list")

numbers = [2, 4, 6, 8, 10]
target = int(input("Enter a number to search: "))

for num in numbers:
    if num == target:
        print(target, "found in the list!")
        break
else:
    print(target, "not found in the list.")

# -------------------------------

# ✅ Summary:
# - The `else` block after `for` runs **only if the loop completes without `break`**.
# - Useful for search tasks where you want to know if the loop exited normally.
