class LRUCache:
    # Define a class to represent the items in the cache.
    # The items have a key, a value, and pointers to the previous and next items in the linked list.
    class Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        # Initialize the cache with the given capacity.
        self.capacity = capacity
        # Use a dictionary to store the items in the cache.
        # The keys in the dictionary are the keys of the items,
        # and the values in the dictionary are the values of the items.
        self.cache = {}
        # Use a doubly-linked list to track the order of the items in the cache.
        # The head of the linked list is the least recently used item,
        # and the tail of the linked list is the most recently used item.
        self.head = None
        self.tail = None

    def get(self, key):
        # Return None if the key does not exist in the cache.
        if key not in self.cache:
            return None

        # Move the item to the tail of the linked list.
        item = self.cache[key]
        self.remove(item)
        self.add_to_tail(item)

        # Return the value of the item.
        return item.value

    def put(self, key, value):
        # If the key already exists in the cache, update the value and move the item to the tail of the linked list.
        if key in self.cache:
            item = self.cache[key]
            item.value = value
            self.remove(item)
            self.add_to_tail(item)
            return

        # If the cache is full, remove the least recently used item from the cache and the linked list.
        if len(self.cache) == self.capacity:
            self.remove_head()

        # Create a new item and add it to the cache and the linked list.
        item = Item(key, value)
        self.cache[key] = item
        self.add_to_tail(item)

    def remove(self, item):
        # Remove the item from the linked list.
        if item.prev is not None:
            item.prev.next = item.next
        if item.next is not None:
            item.next.prev = item.prev
        if item == self.head:
            self.head = item.next
        if item == self.tail:
            self.tail = item.prev

        # Remove the item from the cache.
        del self.cache[item.key]


"""
The remove method removes the given item from the linked list and the cache. 
It updates the pointers of the previous and next items in the linked list, and updates the head and tail of the linked list 
if necessary. It then removes the item from the cache using the key of the item.
"""
