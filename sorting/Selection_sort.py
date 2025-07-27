# Initial unsorted list
list = [2, 8, 5, 6, 4, 9, 1]

def sort(list):
    # Outer loop: iterate over each position in the list
    # At each step, we will place the smallest remaining element in position i
    for i in range(len(list)-1):
        # Assume the current position i has the smallest value
        minpos = i

        # Inner loop: find the smallest element in the remaining unsorted part
        for j in range(i, len(list)):
            if list[j] < list[minpos]:
                # Update minpos if we find a smaller element
                minpos = j

        # After inner loop, swap the smallest element with the element at position i
        temp = list[minpos]
        list[minpos] = list[i]
        list[i] = temp
        # After this swap, the first i+1 elements are sorted

# Call the sort function
sort(list)

# Print the sorted list
print(list)  # Output: [1, 2, 4, 5, 6, 8, 9]
