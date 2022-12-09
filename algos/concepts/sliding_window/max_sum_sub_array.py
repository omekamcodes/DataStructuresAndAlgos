"""
To find the maximum sum of any contiguous subarray of size k in an array of positive numbers, 
you can use a sliding window approach. 
This involves keeping track of the sum of the current window of 
size k and updating the sum as 
the window moves through the array.
"""


def max_sub_array_of_size_k(k, arr):
    # Initialize the maximum sum to be the sum of the first k elements of the array.
    max_sum = sum(arr[:k])

    # Iterate over the array, starting at the kth element.
    # For each element, update the sum of the current window by subtracting the first element in the window
    # and adding the current element.
    # Update the maximum sum if the current sum is greater than the maximum sum.
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum


"""
The max_sub_array_of_size_k function will return the maximum sum of 
any contiguous subarray of size k in the given array. 
In this example, the maximum sum of any contiguous subarray 
of size 3 is 8 (from the subarray [5, 1, 3]).
"""

k = 3
arr = [2, 1, 5, 1, 3, 2]
max_sum = max_sub_array_of_size_k(k, arr)
