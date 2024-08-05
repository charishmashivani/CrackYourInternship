#Day 19

import heapq

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        min_heap = []
        seen = set()
        
        heapq.heappush(min_heap, 1)
        seen.add(1)
        
        ugly_number = 1
        
        for _ in range(n):
            ugly_number = heapq.heappop(min_heap)
            
            for factor in [2, 3, 5]:
                new_ugly = ugly_number * factor
                if new_ugly not in seen:
                    heapq.heappush(min_heap, new_ugly)
                    seen.add(new_ugly)
        
        return ugly_number
