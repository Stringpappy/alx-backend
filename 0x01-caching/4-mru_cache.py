#!/usr/bin/python3
"""
caching module
"""
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """MRU Cache class that inherits from BaseCaching."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()  
        self.cache_data = {}  
        self.order = []  

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return  

        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)  
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.order.pop()  
                del self.cache_data[mru_key]  
                print(f"DISCARD: {mru_key}")  

            self.cache_data[key] = item
        self.order.append(key)  

    def get(self, key):
        """Get an item from the cache."""
        if key is None or key not in self.cache_data:
            return None  

        return self.cache_data[key]  

