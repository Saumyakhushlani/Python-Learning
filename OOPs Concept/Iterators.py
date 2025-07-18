# This file demonstrates:
# 1. Iterating a list using index and for loop
# 2. Using an iterator object with next()
# 3. Creating your own custom iterator class
# ----------------------------------------------

# ----------------------------------------------
# PART 1: ITERATING OVER A LIST
# ----------------------------------------------
nums = [7, 6, 5, 4]

# Using index-based iteration
for i in range(len(nums)):
    print(nums[i])  # Prints elements one by one using index

# ----------------------------------------------
# PART 2: CONVERTING LIST TO ITERATOR
# ----------------------------------------------
# Create an iterator from the list
it = iter(nums)

print(it)  # Prints the iterator object (its memory address)

# Fetch values using __next__() or next()
print(it.__next__())  # 7
print(it.__next__())  # 6
print(it.__next__())  # 5

# Or simply use the built-in next() function
print(next(it))       # 4 (next element)

# ----------------------------------------------
# PART 3: CREATING YOUR OWN ITERATOR
# ----------------------------------------------
# We want an iterator that yields numbers from 1 to 10.

class Top10:
    def __init__(self):
        # Start counting from 1
        self.num = 1

    def __iter__(self):
        # __iter__ must return the iterator object itself
        return self

    def __next__(self):
        # Yield values from 1 to 10
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            # When no more items are left, raise StopIteration
            raise StopIteration

# ----------------------------------------------
# USING THE CUSTOM ITERATOR
# ----------------------------------------------
values = Top10()  # Create an instance (iterator object)

# You can manually fetch next values:
print(next(values))  # 1
print(next(values))  # 2

# Or use in a for loop (which internally calls next()):
for i in values:
    print(i)  # Prints 3 to 10, because 1 and 2 were already fetched above

# NOTE:
# Once values are consumed from an iterator, they are NOT reset.
# If you want to start over, you must create a new iterator instance.
