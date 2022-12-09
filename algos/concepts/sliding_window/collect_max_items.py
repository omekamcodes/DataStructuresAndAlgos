"""
Question: You are visiting a row of houses to collect items. 
Each house has a different type of item. 
You will be given two bags, and 
your goal is to collect as many items as possible to be placed 
in the given bags.

You will be given an array of strings,
 where each string represents a house. 
 The row of houses has the following restrictions:

Each bag can have only one type of item.
There is no limit to how many items a bag can hold.
You can start with any house, but you cannot skip a house once you have started.
You will collect exactly one item from every house until you cannot, i.e., 
you will stop when you have to collect from a third item type.
Write a function collect_maximum_number_of_items to return the maximum number of items that can be collected in the given bags.
"""


def collect_maximum_number_of_items(arr):
    # Initialize the maximum number of items to be 0.
    max_items = 0

    # Initialize the start and end indices of the window to be 0.
    start_index = 0
    end_index = 0

    # Initialize a dictionary to store the count of each item type in the window.
    item_count = {}

    # Iterate over the array, starting at the first element.
    # For each element, update the count of the item type in the window.
    # If the current number of distinct item types in the window is greater than 2,
    # move the start index of the window forward until the number of distinct item types
    # is less than or equal to 2.
    # Update the maximum number of items if the current number is greater than the maximum number.
    for i in range(len(arr)):
        item = arr[i]
        item_count[item] = item_count.get(item, 0) + 1
        while len(item_count) > 2:
            item = arr[start_index]
            item_count[item] -= 1
            if item_count[item] == 0:
                del item_count[item]
            start_index += 1
        max_items = max(max_items, i - start_index + 1)

    return max_items


arr = ["house1", "house2", "house3", "house1", "house3"]
max_items = collect_maximum_number_of_items(arr)

"""
The collect_maximum_number_of_items function will 
return the maximum number of items that can be 
collected from the given houses. In this example, the maximum number of 
items that can be collected is 3, which can be achieved by collecting one item from "house1", 
one item from "house2", and one item from "house3".
"""


"""
item_count[item] = item_count.get(item, 0) + 1 is a statement that updates the count of a particular item type in the window.
The get method is called on the item_count dictionary, with the item and 0 as arguments. 
This returns the value associated with the item key in the dictionary, or 0 if the item key is not in the dictionary.
"""
