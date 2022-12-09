"""
To find the length of the smallest contiguous subarray whose sum is greater than or equal to S in an array of positive numbers, 
you can use a similar sliding window approach as max_sum_sub_array.py
However, instead of keeping track of the maximum sum, 
you can keep track of the minimum length of a subarray that 
has a sum greater than or equal to S.
"""


def smallest_subarray_with_given_sum(S, arr):
    # Initialize the minimum length to be the length of the array.
    min_length = len(arr)

    # Initialize the sum of the current window to be 0.
    window_sum = 0

    # Initialize the start and end indices of the window to be 0 and -1, respectively.
    # This is because the window has not yet been defined.
    start_index = 0
    end_index = -1

    # For each element, update the sum of the current window by adding the current element.
    # If the current sum is greater than or equal to S, update the minimum length.
    # Then, while the current sum is greater than or equal to S, move the start index of the window forward
    # and subtract the element at the start index from the current sum.
    for i in range(len(arr)):
        window_sum += arr[i]
        if window_sum >= S:
            min_length = min(min_length, i - start_index + 1)
            while window_sum >= S:
                start_index += 1
                window_sum -= arr[start_index]

    # If the minimum length is still the length of the array, return 0
    # because no subarray with a sum greater than or equal to S was found.
    # Otherwise, return the minimum length.
    return 0 if min_length == len(arr) else min_length


S = 7
arr = [2, 1, 5, 2, 3, 2]
min_length = smallest_subarray_with_given_sum(S, arr)

# The smallest subarray with a sum greater than or equal to S is [5, 2] with a length of 2.
# Therefore, the function should return 2.
assert min_length == 2

"""
This test case checks that the function returns the correct 
minimum length of the smallest subarray with a sum greater 
than or equal to S. 
The input S is 7 and the array is [2, 1, 5, 2, 3, 2]. The smallest subarray with a sum greater than or equal to S is [5, 2] with a length of 2. 
Therefore, the function should return 2.
"""
