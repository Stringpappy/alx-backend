#!/usr/bin/python3
from BaseCaching import BaseCaching

class LRUCache(BaseCaching):
    """LRU Cache class that inherits from BaseCaching."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.cache_data = {}
        self.order = []  # Keep track of the order of access

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item and mark it as recently used
            self.cache_data[key] = item
            self.order.remove(key)  # Remove the key from its current position
            self.order.append(key)   # Re-add it to mark it as most recently used
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the least recently used item (the first in the order list)
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]  # Remove it from the cache
                print(f"DISCARD: {lru_key}")

            # Add the new key-value pair
            self.cache_data[key] = item
            self.order.append(key)  # Add the new key to the order list

    def get(self, key):
        """Get an item from the cache."""
        if key is None or key not in self.cache_data:
            return None

        # Mark this key as recently used by moving it to the end
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
