# --------------------------------------------
# Linear Search using FOR loop
# --------------------------------------------

my_list = [5, 6, 4, 8, 7, 2, 6, 9]
n = 9  # element to search

def search(lst, n):
    # iterate over list with index and value
    for i, value in enumerate(lst):
        if value == n:
            return i  # return index if found
    return -1  # not found

pos = search(my_list, n)

if pos != -1:
    print(f"✅ Element {n} found at index {pos} (position {pos+1})")
else:
    print(f"❌ Element {n} not found in the list.")
