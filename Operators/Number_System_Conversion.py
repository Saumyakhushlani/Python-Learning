# ---------------------------
# Binary to Decimal Conversion
# ---------------------------

# Method 1: Using built-in int()
binary_str = "1010"
decimal_val = int(binary_str, 2)  # base 2
print("Binary to Decimal (built-in):")
print("Binary: {binary_str} => Decimal: {decimal_val}")

# Method 2: Manual Conversion
binary_str = "1101"
decimal_val_manual = 0
for i in range(len(binary_str)):
    bit = int(binary_str[-(i + 1)])  # Right to left
    decimal_val_manual += bit * (2 ** i)

print("Binary to Decimal (manual):")
print("Binary: {binary_str} => Decimal: {decimal_val_manual}")

# ---------------------------
# Decimal to Binary Conversion
# ---------------------------

# Method 1: Using built-in bin()
decimal_num = 13
binary_str = bin(decimal_num)[2:]  # Remove '0b' prefix
# 0B comes in prefix to prove that the number is binary
print("\nDecimal to Binary (built-in):")
print(f"Decimal: {decimal_num} => Binary: {binary_str}")

# Method 2: Manual Conversion
decimal_num = 10
binary_digits = []
temp = decimal_num

while temp > 0:
    binary_digits.append(str(temp % 2))
    temp = temp // 2

binary_manual = ''.join(reversed(binary_digits))

print("Decimal to Binary (manual):")
print("Decimal: {decimal_num} => Binary: {binary_manual}")

# Similarly for octal system we can use
oct(25)
#0o31
# the prefix zero O represents that the number is in octal form

# Similarly for octal system we can use
hex(25)