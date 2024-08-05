#Day 19

import heapq

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        min_heap = []
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(min_heap, diff)
                
                if len(min_heap) > ladders:
                    smallest_jump = heapq.heappop(min_heap)
                    bricks -= smallest_jump
                    if bricks < 0:
                        return i
        
        return len(heights) - 1
