#Day 19

import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        prev_char = ''
        prev_count = 0
        result = []
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            prev_char = char
            prev_count = count + 1
        
        if len(result) == len(s):
            return ''.join(result)
        else:
            return ""
