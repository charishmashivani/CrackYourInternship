#Day 32

import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph = {i: [] for i in range(n)}
        for u, v, price in flights:
            graph[u].append((v, price))
        
        pq = [(0, src, 0)]
        
        dist = {(src, 0): 0}
        
        while pq:
            cost, city, stops = heapq.heappop(pq)
            
            if city == dst:
                return cost
            
            if stops > k:
                continue
            
            for neighbor, price in graph[city]:
                new_cost = cost + price
                if (neighbor, stops + 1) not in dist or new_cost < dist[(neighbor, stops + 1)]:
                    dist[(neighbor, stops + 1)] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, stops + 1))
        
        return -1
