# In the earlier video we learned about Iterators.
# Now we learn about Generators – a simpler way to create iterators.
# ------------------------------------------------------
# Key points:
# ✅ A generator function uses the special keyword `yield`
# ✅ `yield` makes the function return an iterator (a generator object)
# ✅ Each time `next()` is called on the generator, execution resumes from the last yield
# ✅ Unlike `return`, `yield` does NOT terminate the function after giving one value
# ✅ Generators are memory efficient for large sequences

# ------------------------------------------------------
# Example 1: Simple generator yielding fixed values
# ------------------------------------------------------

def top_values():
    # instead of return, we use yield to create a generator
    yield 1
    yield 2
    yield 3
    yield 4

# Create a generator object
vals = top_values()

# Fetch values one by one using next()
print(next(vals))  # prints 1
print(next(vals))  # prints 2

# We can also use a for loop to exhaust remaining values
for v in vals:
    print(v)  # prints 3 and 4


# ------------------------------------------------------
# Example 2: Generator yielding first 10 perfect squares
# ------------------------------------------------------

def perfect_squares():
    n = 1
    # we want top 10 squares
    while n <= 10:
        sk = n * n
        yield sk       # yield the square
        n += 1         # move to next number

# Create a generator object
squares = perfect_squares()

# Iterate through generator in a loop
print("Top 10 perfect squares:")
for s in squares:
    print(s)


# ------------------------------------------------------
# Why use generators?
# ------------------------------------------------------
# 👉 They don’t store all results in memory at once.
# 👉 They yield one value at a time, perfect for large datasets.
# 👉 Example: Fetching 1000 database records without loading all at once.

# ------------------------------------------------------
# Notes:
# * yield ≈ return + “pause & remember state”
# * After yield, function execution is suspended and resumes on next() call
# * Generators automatically implement __iter__() and __next__(), no need to write a class
