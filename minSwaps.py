#Day 15

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        n = len(nums)
        arr = sorted((num, i) for i, num in enumerate(nums))
        
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arr[i][1] == i:
                continue

            cycle_size = 0
            x = i
            
            while not visited[x]:
                visited[x] = True
                x = arr[x][1]
                cycle_size += 1
            
            if cycle_size > 0:
                swaps += (cycle_size - 1)
        
        return swaps
