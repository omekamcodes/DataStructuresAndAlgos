def searchQuadruplets(arr, target):
    arr.sort()

    quadruplets = []
    for i in range(len(arr)):
        # avoid duplicates
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, len(arr)):
            # avoid duplicates
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            left = j + 1
            right = len(arr) - 1
            while left < right:
                sum = arr[i] + arr[j] + arr[left] + arr[right]
                if sum == target:
                    quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1

                    # skip duplicate quadruplets
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1

    return quadruplets


# example 1
numbers = [4, 1, 2, -1, 1, -3]
target = 1
print(searchQuadruplets(numbers, target))
# output: [[-3, -1, 1, 4], [-3, 1, 1, 2]]

# example 2
numbers = [2, 0, -1, 1, -2, 2]
target = 2
print(searchQuadruplets(numbers, target))
# output: [[-2, 0, 2, 2], [-1, 0, 1, 2]]


"""
To solve this problem, we can use a brute-force approach where we consider all possible quadruplets and check if their sum is equal to the target number. 
This approach would be inefficient as it would take O(n^4) time, where n is the length of the input array.

A better approach would be to first sort the array. 
This will make it easier to find the quadruplets that sum up to the target number. 
After sorting the array, we can iterate over the elements of the array and for each element, 
we can use two pointers to find the other three elements that sum up to the target number. This approach would take O(n^2) time, which is much faster than the brute-force approach.

Here is the detailed algorithm:

Sort the input array in ascending order.
Iterate over the elements of the array, and for each element, use two pointers to find the other three elements that sum up to the target number.
To avoid duplicates, skip any element that is the same as the previous element.
Return the unique quadruplets that sum up to the target number.
"""


"""
Deep Explain:

Suppose we have the array [4, 1, 2, -1, 1, -3] and the target number is 1. 
We first sort the array, which gives us [-3, -1, 1, 1, 2, 4]. 
Then, we iterate over the elements of the array and use two pointers to find 
the other three elements that sum up to the target number.

At the first step, we have the element -3 and we use two pointers left and right to find the other 
three elements that sum up to the target number.
 We initialize left to the index of the next element after -3, which is -1, 
 and right to the index of the last element, which is 4. Since -3 + -1 + 1 + 4 = 1, 
 which is the target number, we have found a quadruplet [-3, -1, 1, 4] that sums up to the target number. We then move the left and right pointers to the next elements, which are 1 and 2, respectively. 
 Since -3 + -1 + 1 + 2 = -1, which is not the target number, we continue moving the pointers.
  We then move the left pointer to the next element, which is 2, and the right pointer to the next-to-last element, which is 1. Since -3 + -1 + 2 + 1 = -1, which is not the target number, we continue moving the pointers. At this point, the left pointer is at the last element, which is 4, and the right pointer is at the second-to-last element, which is 2. Since -3 + -1 + 4 + 2 = 2, which is not the target number, we continue moving the pointers. Since the left and right pointers have crossed each other, we have exhausted all possibilities and we move on to the next element.

At the second step, we have the element -1 and we use two pointers to find the other 
three elements that sum up to the target number. We initialize left to the index of the next element after -1, which is 1, and right to the index of the last element, which is 4. Since -1 + 1 + 1 + 4 = 5, which is not the target number, we continue moving the pointers. We then move the left pointer to the next element, which is 2, and the right pointer to the next-to-last element, which is 1. Since -1 + 1 + 2 + 1 = 3, which is not the target number, we continue moving the pointers. At this point, the left pointer is at the last element, which is 4, and the right pointer is at the second-to-last element, which is 2. Since -1 + 1 + 4 + 2 = 6, which is not the target number, we continue moving the pointers. Since the left and right pointers have crossed each other, we have exhausted all possibilities and we move on to the next element.

At the third step, we have the element 1 and we use two pointers to find the 
other three elements that sum up to the target number. We initialize left to the index of the next element after 1, which is 1, and right to the index of the last element, which is 4. Since 1 + 1 + 1 + 4 = 7, which is not the target number, we continue moving the pointers. We then move the left pointer to the next element, which is 2, and the right pointer to the next-to-last element, which is 1. Since 1 + 1 + 2 + 1 = 5, which is not the target number, we continue moving
"""
