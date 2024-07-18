class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        n=len(nums)
        return nums[n//2]
        """
        :type nums: List[int]
        :rtype: int
        """
        
