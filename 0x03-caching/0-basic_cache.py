#!/usr/bin/python3
'''Basic Cache Module'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Basic Cache Sytem Class'''
    def put(self, key, item):
        '''Adding itrm to cache'''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''Obtain an item from cahce'''
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
