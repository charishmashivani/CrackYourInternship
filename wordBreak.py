#Day 22

#User function Template for python3

class Solution:
    def wordBreak(self, A, B):
        word_set = set(B)
        n = len(A)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and A[j:i] in word_set:
                    dp[i] = True
                    break
        
        return 1 if dp[n] else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		ob=Solution()
		res = ob.wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends
