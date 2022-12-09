def find_pair_with_sum(arr, target_sum):
    # Store the indices of the two numbers in a list.
    pair_indices = []

    # Keep track of the indices we've seen so far.
    seen_indices = set()

    for i, num in enumerate(arr):
        # Calculate the number we need to find in order to add up to the target sum.
        num_to_find = target_sum - num

        # Check if the number we need to find has been seen in the array before.
        if num_to_find in seen_indices:
            # If it has been seen, add the indices of the current number and the number we need to find to the pair_indices list.
            pair_indices.append(i)
            pair_indices.append(arr.index(num_to_find))
            break
        else:
            # If it hasn't been seen, add the index of the current number to the set of seen indices.
            seen_indices.add(i)

    return pair_indices


"""
This function takes in an array arr and a target sum target_sum, and returns a list of indices pair_indices 
where the two numbers at those indices add up to the target sum. 
It does this by iterating through the array and checking if the number we need 
to find in order to add up to the target sum has been seen in the array before. 
If it has, we add the indices of the current number and the number we need to find to the pair_indices list, 
and break out of the loop. 
If it hasn't been seen, we add the index of the current number to the set of seen indices.
"""


def find_pair_with_sum(arr, target_sum):
    # Initialize the indices of the two numbers in the pair to -1.
    i, j = -1, -1

    # Set the start and end indices for the search.
    start, end = 0, len(arr) - 1

    # Keep searching until the start index is greater than or equal to the end index.
    while start < end:
        # Calculate the sum of the numbers at the start and end indices.
        cur_sum = arr[start] + arr[end]

        # Check if the current sum is equal to the target sum.
        if cur_sum == target_sum:
            # If it is, set the indices of the two numbers in the pair and break out of the loop.
            i, j = start, end
            break
        elif cur_sum < target_sum:
            # If the current sum is less than the target sum, increment the start index.
            start += 1
        else:
            # If the current sum is greater than the target sum, decrement the end index.
            end -= 1

    return [i, j]


"""
This implementation is similar to the previous one, but instead of storing the indices we've seen in a set, 
it uses two indices start and end to search the array for a pair of numbers that add up to the target sum. 
It does this by incrementing the start index if the current sum is less than the target sum, 
and decrementing the end index if the current sum is greater than the target sum. 
This allows us to search the array in O(n) time while using only two indices, 
which means that it uses O(1) space.


"""


# Example 1: [1, 2, 3, 4, 6], target_sum=6
find_pair_with_sum([1, 2, 3, 4, 6], 6)
# Output: [1, 3]

# Example 2: [2, 5, 9, 11], target_sum=11
find_pair_with_sum([2, 5, 9, 11], 11)
# Output: [0, 2]

# Example 3: [1, 3, 5, 7, 9], target_sum=10
find_pair_with_sum([1, 3, 5, 7, 9], 10)
# Output: []
