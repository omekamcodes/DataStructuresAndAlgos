class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    def __init__(self, size):
        # Initialize an array to store the items in the hash map.
        # The size of the array should be a prime number to avoid collisions.
        self.size = size
        self.table = [None] * self.size

    def hash(self, key):
        # Generate a hash value for the given key using the modulo operator.
        return hash(key) % self.size

    def put(self, node):
        # Generate a hash value for the given key.
        h = self.hash(node.key)
        # If the hash value is not already in the hash map, insert it.
        if self.table[h] is None:
            self.table[h] = node
        else:
            # If the hash value is already in the hash map, update the value.
            self.table[h] = node

    def get(self, key):
        # Generate a hash value for the given key.
        h = self.hash(key)
        # Return the value for the hash value in the hash map, or None if it does not exist.
        return self.table[h].value if self.table[h] is not None else None


# To use the HashMap class, you can initialize a new instance of the class by specifying the size of the hash map:
hash_map = HashMap(101)

# You can then create Node objects to store the items in the hash map, and use the put method to insert or update the items in the hash map:

node1 = Node("key1", "value1")
node2 = Node("key2", "value2")

hash_map.put(node1)
hash_map.put(node2)

print(hash_map.get("key1"))  # Output: 'value1'
print(hash_map.get("key2"))  # Output: 'value2'
