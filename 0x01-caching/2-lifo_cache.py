#!/usr/bin/python3
"""
A class `LIFOCache` that inherits from `BaseCaching` and is a caching system.
"""

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    You must use `self.cache_data` - dictionary from the parent class
    `BaseCaching`
    """

    def __init__(self):
        """
        Init
        """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """
        Must assign to the dictionary `self.cache_data` the item value for
        the key `key`.
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.is_full():
                self.evict()
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in `self.cache_data` linked to `key`.
        """
        return self.cache_data.get(key, None)

    def is_full(self):
        """
        If the number of items in `self.cache_data` is higher that
        `BaseCaching.MAX_ITEMS`
        """
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """
        you must print 'DISCARD:' with the key discarded and following by a
        new line -pop-
        """
        popped = self.queue.pop()
        del self.cache_data[popped]
        print("DISCARD: " + str(popped))
