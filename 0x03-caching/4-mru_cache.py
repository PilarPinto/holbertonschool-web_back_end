#!/usr/bin/python3
'''MRU Cache System Module'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    ''' Cache System MRU'''
    def __init__(self):
        self.counter = 0
        self.ages = {}
        super().__init__()

    def put(self, key, item):
        '''Adding item definition'''
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_pop = sorted(self.ages.items(),
                                key=lambda x: x[1], reverse=True)[0][0]
                self.cache_data.pop(to_pop)
                self.ages.pop(to_pop)
                print('DISCARD:', to_pop)

            self.ages[key] = self.counter
            self.counter += 1

    def get(self, key):
        '''Get an item form key'''
        if key and key in self.cache_data:
            self.ages[key] = self.counter
            self.counter += 1
            return self.cache_data.get(key)
        return None
