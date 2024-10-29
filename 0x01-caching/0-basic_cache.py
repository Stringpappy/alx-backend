#!/usr/bin/env python3
"""module that Create a class BasicCache that inherits
from BaseCaching and is a caching system"""
from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching."""

    def __init__(self):
        """initialise the class """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache."""
        return self.cache_data.get(key, None)
