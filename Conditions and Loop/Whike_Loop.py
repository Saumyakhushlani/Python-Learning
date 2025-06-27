# ===============================
# while Loop in Python - Basics
# ===============================

# ✅ Basic while loop
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1  # increase count by 1

# ✅ while loop with user input
password = ""
while password != "open123":
    password = input("Enter the password: ")
print("Access granted!")

# ✅ Infinite loop with break
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Loop stopped.")
        break
    print("You entered:", num)

# ✅ while with continue
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # skip even numbers
    print("Odd number:", i)

# ✅ Using while loop to sum numbers
total = 0
n = int(input("How many numbers to add? "))
count = 0
while count < n:
    num = int(input(f"Enter number {count+1}: "))
    total += num
    count += 1
print("Total sum is:", total)
