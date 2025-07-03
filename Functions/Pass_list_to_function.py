def count(l):
    even = 0
    odd = 0
    for i in l:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

print("Enter the values in the list")
l = list(map(int, input().split()))

even, odd = count(l)

# .format() is used to insert the values of 'even' and 'odd' into the string at the {} placeholders
print("Even : {} , Odd : {}".format(even, odd))
