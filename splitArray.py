#Day 18

class Solution:
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canSplit(max_sum):
            current_sum = 0
            required_subarrays = 1
            
            for num in nums:
                if current_sum + num > max_sum:
                    required_subarrays += 1
                    current_sum = num
                    if required_subarrays > k:
                        return False
                else:
                    current_sum += num
            
            return True
        
        low = max(nums)
        high = sum(nums)
        
        while low < high:
            mid = (low + high) // 2
            if canSplit(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
