#Day 19

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]
