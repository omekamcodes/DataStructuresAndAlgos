def remove_duplicates(arr):
    # Check if the array is empty.
    if not arr:
        return 0

    # Set the index of the last unique number we've seen to 0.
    last_unique = 0

    # Loop through the array starting from the second element.
    for i in range(1, len(arr)):
        # Check if the current number is different from the previous one.
        if arr[i] != arr[last_unique]:
            # If it is, increment the index of the last unique number and set the element at that index
            # to the current number.
            last_unique += 1
            arr[last_unique] = arr[i]

    # Return the new length of the array by adding 1 to the index of the last unique number we've seen.
    return last_unique + 1


"""
This implementation loops through the array starting from the second element, and uses the last_unique variable to keep track of the index of the 
last unique number we've seen. 
If the current number is different from the previous one, 
it increments the last_unique index and sets the element at that index to the current number. 
This allows us to remove all duplicates from the array in-place, without using any extra space.
"""

# Example 1: [2, 3, 3, 3, 6, 9, 9]
remove_duplicates([2, 3, 3, 3, 6, 9, 9])
# Output: 4
# Array after removing duplicates: [2, 3, 6, 9]

# Example 2: [2, 2, 2, 11]
remove_duplicates([2, 2, 2, 11])
# Output: 2
# Array after removing duplicates: [2, 11]

# Example 3: [5, 7, 11, 11, 11, 12]
remove_duplicates([5, 7, 11, 11, 11, 12])
# Output: 4
# Array after removing duplicates: [5, 7, 11, 12]
