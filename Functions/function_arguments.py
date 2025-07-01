def modify_number(x):
    print("Inside function (before):", x)             # ➤ Will print: 5
    print("ID inside (before):", id(x))               # ➤ Same as ID outside (before)

    x = x + 10  # This creates a NEW integer object (because int is immutable)
    
    print("Inside function (after):", x)              # ➤ Will print: 15
    print("ID inside (after):", id(x))                # ➤ Different from ID inside (before)

# Main program
num = 5
print("Before calling function:", num)                # ➤ Will print: 5
print("ID outside (before):", id(num))                # ➤ ID of 5

modify_number(num)

print("After calling function:", num)                 # ➤ Still prints: 5
print("ID outside (after):", id(num))                 # ➤ Same as ID outside (before)

#This is because we are using int which is immutable but if we use mutble like list
#If we use list the values gets updated in the list also but id at every place remains the same.