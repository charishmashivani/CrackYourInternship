#Day 1

class Solution(object):
    def moveZeroes(self, nums):
        n = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[n] = nums[n], nums[i]
                n+=1
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
