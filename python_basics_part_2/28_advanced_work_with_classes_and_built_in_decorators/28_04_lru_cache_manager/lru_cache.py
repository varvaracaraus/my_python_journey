from collections import OrderedDict
from typing import Optional


class LRUCache:
    """
    LRU Cache class that stores a limited number of objects and removes the least recently used items when the
    limit is exceeded.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: str) -> Optional[str]:
        """
        Returns the value for the given key if it exists in the cache. Otherwise, returns None.
        """
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)  # Move the key to the end to show that it was recently used
        return self.cache[key]

    @property
    def oldest(self) -> Optional[str]:
        """
        Returns the oldest item from the cache.
        """
        return next(iter(self.cache), None)

    @oldest.setter
    def oldest(self, new_elem: tuple[str, str]):
        """
        Adds a new element to the cache. If the cache exceeds its capacity, removes the oldest item.
        """
        key, value = new_elem
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def print_cache(self):
        """
        Prints the current state of the cache.
        """
        print("LRU Cache:")
        for key, value in self.cache.items():
            print(f"{key} : {value}")
