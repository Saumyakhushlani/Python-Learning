# Initial unsorted list
list = [10, 88, 51, 69, 1, 58, 23]

# For binary search, the array must be sorted
list.sort()   # Sorts the list in ascending order

# Element to search
search = 58

# If the element is not found, we will keep index as -1
index = -1

# Set the initial lower bound and upper bound
low = 0                # starting index of the list
high = len(list) - 1   # ending index of the list

# Binary search loop
while low <= high:     # Continue searching as long as the range is valid
    mid = (low + high) // 2    # Find the middle index

    if search > list[mid]:
        # If the search element is greater than the middle element,
        # discard the left half and search in the right half
        low = mid + 1
    elif search < list[mid]:
        # If the search element is smaller than the middle element,
        # discard the right half and search in the left half
        high = mid - 1
    else:
        # Element found at index mid
        index = mid
        break              # Exit the loop once we find the element

# Print the result
print(index)  # Will print the index if found, otherwise -1
