def sort(nums):
    # Outer loop: controls how many passes we need
    # Starts from the last index and moves backward to 1
    # After each pass, the largest element gets bubbled to the end
    for i in range(len(nums)-1, 0, -1):
        # Inner loop: compares adjacent elements up to the current i
        # We only go till 'i' because elements after i are already sorted
        for j in range(i):
            # If the current element is greater than the next element, swap them
            if nums[j] > nums[j+1]:
                # Perform swapping using a temporary variable
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp
    # Return the sorted list
    return nums

# Example usage
nums = [2, 8, 5, 6, 4, 1]  # Unsorted list
nums = sort(nums)          # Call bubble sort
print(nums)                # Output: [1, 2, 4, 5, 6, 8]
