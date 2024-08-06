#Day 20

import random
from collections import defaultdict

class RandomizedCollection(object):
    def __init__(self):
        self.elements = []
        self.index_map = defaultdict(set)

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        self.elements.append(val)
        self.index_map[val].add(len(self.elements) - 1)
        return len(self.index_map[val]) == 1

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not self.index_map[val]:
            return False
        
        remove_idx = self.index_map[val].pop()
        last_element = self.elements[-1]
        
        self.elements[remove_idx] = last_element
        self.index_map[last_element].add(remove_idx)
        
        self.index_map[last_element].remove(len(self.elements) - 1)
        
        self.elements.pop()
        
        if not self.index_map[val]:
            del self.index_map[val]
        
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.elements)
