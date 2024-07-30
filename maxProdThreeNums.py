#Day 2

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = float('inf')
        min2 = float('inf')
        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')
        if len(nums) < 3:
            return 0
        
        for num in nums:
            if num < 0:
                if num < min2:
                    if num <= min1:
                        min2 = min1
                        min1 = num
                    else:
                        min2 = num
            if num > max3:
                if num > max2:
                    if num >= max1:
                        max3 = max2
                        max2 = max1
                        max1 = num
                    else:
                        max3 = max2
                        max2 = num
                else:
                    max3 = num

        if min1 <= 0 and min2 <= 0 and max1 >= 0 and min1 * min2 > max2*max3:
            return min1 * min2 * max1
        return max1 * max2 * max3
        """
        :type nums: List[int]
        :rtype: int
        """
        
