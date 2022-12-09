" Given an array of unsorted numbers, find all unique triplets in it that add up to zero."

"""
Sort the input array in ascending order.
Iterate over the elements of the array, and for each element, use two pointers to find the other two elements that sum up to zero.
To avoid duplicates, skip any element that is the same as the previous element.
Return the unique triplets that sum up to zero.
"""


def searchTriplets(arr):
    arr.sort()

    triplets = []
    for i in range(len(arr)):
        # avoid duplicates
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = len(arr) - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == 0:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

                # skip duplicate triplets
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1

    return triplets


# example 1
arr = [-3, 0, 1, 2, -1, 1, -2]
print(searchTriplets(arr))
# output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]

# example 2
arr = [-5, 2, -1, -2, 3]
print(searchTriplets(arr))
# output: [[-5, 2, 3], [-2, -1, 3]]
