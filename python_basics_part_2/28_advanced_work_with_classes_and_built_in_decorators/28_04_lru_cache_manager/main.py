from lru_cache import LRUCache

# Create an instance of LRUCache with a capacity of 4
cache = LRUCache(4)

# Add elements to the cache
cache.oldest = ("key1", "value1")
cache.oldest = ("key2", "value2")
cache.oldest = ("key3", "value3")
cache.oldest = ("key4", "value4")

# Print the current state of the cache
cache.print_cache()  # Expected: key1 : value1, key2 : value2, key3 : value3, key4 : value4

# Retrieve the value for a key
print(f"Value for 'key1': {cache.get('key1')}")  # Expected: Value for 'key1': value1

# Add a new element, which exceeds the capacity, causing the oldest to be removed
cache.oldest = ("key5", "value5")

# Print the updated cache
cache.print_cache()  # Expected: key2 : value2, key3 : value3, key4 : value4, key5 : value5
