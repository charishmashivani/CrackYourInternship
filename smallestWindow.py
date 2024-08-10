#Day 24

from collections import Counter, defaultdict

class Solution(object):
    def smallestWindow(self, s, p):
        
        if not s or not p:
            return "-1"
        
        p_count = Counter(p)
        required = len(p_count)
        
        window_count = defaultdict(int)
        left, right = 0, 0
        formed = 0
        min_len = float('inf')
        min_window = ""
        
        while right < len(s):
            char = s[right]
            window_count[char] += 1
            
            if char in p_count and window_count[char] == p_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]
                
                window_count[char] -= 1
                if char in p_count and window_count[char] < p_count[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return min_window if min_len != float('inf') else "-1"
