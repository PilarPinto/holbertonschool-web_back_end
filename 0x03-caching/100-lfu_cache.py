#!/usr/bin/python3
'''Least recent cache System Module'''
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''A Least Recently Used Cache Sys'''

    def __init__(self):
        '''Constructor'''
        self.counter = 0
        self.ages = {}
        self.used = {}
        super().__init__()

    def count_used(self, key):
        '''Counter and verify if a key exists'''
        if key in self.used:
            self.used[key] += 1
        else:
            self.used[key] = 1

    def put(self, key, item):
        '''Adding item to the cache'''
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_used = min(self.used.values())
                for k, _ in sorted(self.ages.items(),
                                   key=lambda x: x[1]):
                    if self.used[k] == least_used:
                        self.cache_data.pop(k)
                        self.ages.pop(k)
                        self.used.pop(k)
                        break
                print('DISCARD:', k)
            self.ages[key] = self.counter
            self.counter += 1
            self.count_used(key)

    def get(self, key):
        ''' Obtain an item by an input key'''
        if key and key in self.cache_data:
            self.ages[key] = self.counter
            self.counter += 1
            self.count_used(key)
            return self.cache_data.get(key)
        return None
