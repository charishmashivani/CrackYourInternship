#Day 20

#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        prefix_sum = 0
        max_length = 0
        prefix_map = {}
        
        for i in range(n):
            prefix_sum += arr[i]
            
            if prefix_sum == 0:
                max_length = i + 1
            elif prefix_sum in prefix_map:
                max_length = max(max_length, i - prefix_map[prefix_sum])
            else:
                prefix_map[prefix_sum] = i
        
        return max_length

        #Code here


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
