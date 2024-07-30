#Day 13

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                result.append(path)
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    backtrack(end, path + [substring])
        
        result = []
        backtrack(0, [])
        return result
