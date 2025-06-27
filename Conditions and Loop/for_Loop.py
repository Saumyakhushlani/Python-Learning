# ============================
# for Loop in Python - Basics
# ============================

# ✅ Basic for loop using range()
print("Counting from 1 to 5:")
for i in range(1, 6):  # starts from 1, ends at 5
    print(i)

# ✅ Loop from 0 to 4 (default start is 0)
print("Looping 5 times:")
for i in range(5):  # same as range(0, 5)
    print("Iteration", i)

# ✅ Loop with step
#The range here means start from 0 and end at 10 with the step of 2
# The step can be negative also
print("Even numbers from 2 to 10:")
for i in range(2, 11, 2):  # step = 2
    print(i)

# ✅ Looping over a list
fruits = ["apple", "banana", "mango"]
print("Fruits list:")
for fruit in fruits:
    print(fruit)

# ✅ Looping over a string (character by character)
name = "Python"
print("Characters in the word:")
for char in name:
    print(char)

# ✅ Using else with for loop
print("For loop with else:")
for i in range(3):
    print("Number:", i)
else:
    print("Loop finished!")


# ✅ Loop with break
print("Loop with break (stops when i == 3):")
for i in range(5):
    if i == 3:
        break
    print(i)

# ✅ Loop with continue
print("Loop with continue (skips 3):")
for i in range(5):
    if i == 3:
        continue
    print(i)
