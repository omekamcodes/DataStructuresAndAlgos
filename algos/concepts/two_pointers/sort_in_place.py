"""
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects,
    hence, we cant count 0s, 1s, and 2s to recreate the array.
    The flag of the Netherlands consists of three colors: red, white and blue;
    and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.
    Example 1:
    Input: [1, 0, 2, 1, 0]
    Output: [0 0 1 1 2]
    Example 2:
    Input: [2, 2, 0, 1, 2, 0]
    Output: [0 0 1 2 2 2 ]
"""

"""
To solve this problem, we can use a two-pointer approach where we have three pointers: low, mid and high. We initialize low and mid to the first element of the array, and high to the last element of the array. We then iterate over the array until low is less than or equal to high. At each step, we do the following:

If the element at the low pointer is 0, we swap it with the element at the mid pointer and increment both the low and mid pointers.
If the element at the low pointer is 1, we simply increment the low pointer.
If the element at the low pointer is 2, we swap it with the element at the high pointer and decrement the high pointer.
Here is the detailed algorithm:

Initialize three pointers low, mid and high to the first element, the first element, and the last element of the array, respectively.
Iterate over the array until low is less than or equal to high.
If the element at the low pointer is 0, swap it with the element at the mid pointer and increment both low and mid.
If the element at the low pointer is 1, simply increment low.
If the element at the low pointer is 2, swap it with the element at the high pointer and decrement high.

"""


def sort(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


# example 1
arr = [1, 0, 2, 1, 0]
print(sort(arr))
# output: [0, 0, 1, 1, 2]

# example 2
arr = [2, 2, 0, 1, 2, 0]
print(sort(arr))
# output: [0, 0, 1, 2, 2, 2]
