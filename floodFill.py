#Day 15
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        m, n = len(image), len(image[0])
        
        original_color = image[sr][sc]
        
        if original_color == color:
            return image
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != original_color:
                return
            
            image[r][c] = color
            
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        dfs(sr, sc)
        
        return image
