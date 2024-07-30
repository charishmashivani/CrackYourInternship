#Day 2

class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        max_product = float('-inf')
        curr_product = 1

        for i in range(n):
            curr_product *= nums[i]
            max_product = max(max_product, curr_product)
            if curr_product == 0:
                curr_product = 1

        curr_product = 1

        for i in range(n - 1, -1, -1):
            curr_product *= nums[i]
            max_product = max(max_product, curr_product)
            if curr_product == 0:
                curr_product = 1

        return max_product
