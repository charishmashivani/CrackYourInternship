#Day 28

from collections import defaultdict

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        # Step 1: Build the adjacency list for the tree structure
        tree = defaultdict(list)
        for employee, mgr in enumerate(manager):
            if mgr != -1:
                tree[mgr].append(employee)
        
        # Step 2: Perform DFS to calculate the maximum time needed
        def dfs(employee):
            if not tree[employee]:
                return 0
            max_time = 0
            for subordinate in tree[employee]:
                max_time = max(max_time, dfs(subordinate))
            return max_time + informTime[employee]
        
        return dfs(headID)
