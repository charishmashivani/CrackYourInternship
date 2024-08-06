#Day 20

import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        max_heap = []
        
        for point in points:
            x, y = point
            distance = -(x * x + y * y)
            
            heapq.heappush(max_heap, (distance, point))
            
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [point for (_, point) in max_heap]
