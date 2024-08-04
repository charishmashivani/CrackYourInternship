#Day 18

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(set(nums))
        rank = {num: i+1 for i, num in enumerate(sorted_nums)}
        
        def update(index, value):
            while index <= N:
                BIT[index] += value
                index += index & -index
        
        def query(index):
            sum = 0
            while index > 0:
                sum += BIT[index]
                index -= index & -index
            return sum
        
        N = len(sorted_nums)
        BIT = [0] * (N + 1)
        result = []
        
        for num in reversed(nums):
            idx = rank[num]
            result.append(query(idx - 1))
            update(idx, 1)
        
        return result[::-1]
