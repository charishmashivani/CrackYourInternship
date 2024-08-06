#Day 20

class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack = []
        to_remove = len(nums) - k
        
        for num in nums:
            while to_remove > 0 and stack and stack[-1] > num:
                stack.pop()
                to_remove -= 1
            stack.append(num)
        
        return stack[:k]
