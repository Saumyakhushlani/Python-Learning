#----- Complement Operator (~)----------
# The complement operator (~) inverts all bits (0 becomes 1, 1 becomes 0)
# In Python, it also adds 1 to the result and makes it negative due to 2's complement representation.
a = 5         # binary: 0000 0101
result = ~a   # binary: 1111 1010 (in 8-bit), which is -6 in decimal
#Watch video to see about negative numbers
print("~5 =", result)

#----- And Operator (&)----------
# The AND operator compares each bit of two numbers and returns 1 if both bits are 1
a = 5         # binary: 0101
b = 3         # binary: 0011
result = a & b  # binary: 0001 = 1
print("5 & 3 =", result)

#----- Or Operator (|)----------
# The OR operator compares each bit of two numbers and returns 1 if at least one bit is 1
a = 5         # binary: 0101
b = 3         # binary: 0011
result = a | b  # binary: 0111 = 7
print("5 | 3 =", result)

#----- Xor Operator (^)----------
# The XOR operator returns 1 if the bits are different, 0 if they're the same
#Whwn we have odd numbers of one then it returns one 
a = 5         # binary: 0101
b = 3         # binary: 0011
result = a ^ b  # binary: 0110 = 6
print("5 ^ 3 =", result)

#----- Left Shift Operator (<<)----------
# Shifts the bits of a number to the left by a given number of positions
# Each left shift multiplies the number by 2
a = 5         # binary: 0000 0101
result = a << 1  # binary: 0000 1010 = 10
print("5 << 1 =", result)

#----- Right Shift Operator (>>)----------
# Shifts the bits of a number to the right by a given number of positions
# Each right shift divides the number by 2 and discards remainder
a = 5         # binary: 0000 0101
result = a >> 1  # binary: 0000 0010 = 2
print("5 >> 1 =", result)
