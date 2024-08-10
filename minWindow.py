#Day 24

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter, defaultdict
        
        if not s or not t:
            return ""
        
        t_count = Counter(t)
        required = len(t_count)
        
        window_count = defaultdict(int)
        
        left, right = 0, 0
        formed = 0
        min_len = float('inf')
        min_window = ""
        
        while right < len(s):
            char = s[right]
            window_count[char] += 1
            
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]
                
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return min_window
