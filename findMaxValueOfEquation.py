#Day 12

from collections import deque as deq

class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        dq = deq()
        max_value = float('-inf')
        
        for x, y in points:
            while dq and x - dq[0][0] > k:
                dq.popleft()
            if dq:
                max_value = max(max_value, y + x + dq[0][1])
            while dq and y - x >= dq[-1][1]:
                dq.pop()
            
            dq.append((x, y - x))
        
        return max_value
