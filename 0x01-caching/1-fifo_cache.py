#!/usr/bin/env python3
"""
caching module
"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """FIFO Cache class that inherits from BaseCaching."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.cache_data = {}
        self.order = []

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                """ Remove the first item (FIFO)"""
                oldest_key = self.order.pop(0) 
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

        self.cache_data[key] = item
        self.order.append(key)  # Add the key to the order list

    def get(self, key):
        """Get an item from the cache."""
        return self.cache_data.get(key, None)
