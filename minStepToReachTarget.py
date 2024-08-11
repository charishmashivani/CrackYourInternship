#Day 25

from collections import deque

class Solution:
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), 
                 (2, 1), (1, 2), (-1, 2), (-2, 1)]
        
        start = (KnightPos[0] - 1, KnightPos[1] - 1)
        target = (TargetPos[0] - 1, TargetPos[1] - 1)
        
        if start == target:
            return 0
        
        queue = deque([(start[0], start[1], 0)])  # (row, col, steps)
        visited = set()
        visited.add(start)
        
        while queue:
            x, y, steps = queue.popleft()
            
            for move in moves:
                nx, ny = x + move[0], y + move[1]
                
                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                    if (nx, ny) == target:
                        return steps + 1
                    
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
        
        return -1
