#Day 19

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        count = Counter(nums)
        return [item for item, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
        
