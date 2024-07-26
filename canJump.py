#Day 9

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reachable = 0
        n = len(nums)
        
        for i in range(n):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])
            if max_reachable >= n - 1:
                return True
        
        return max_reachable >= n - 1
