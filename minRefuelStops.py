#Day 20

import heapq

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        stations.append([target, 0])
        
        max_heap = []
        curr_fuel = startFuel
        prev_position = 0
        num_stops = 0
        station_index = 0
        
        for position, fuel in stations:
            distance = position - prev_position
            
            curr_fuel -= distance
            
            while curr_fuel < 0 and max_heap:
                curr_fuel -= heapq.heappop(max_heap)
                num_stops += 1
            
            if curr_fuel < 0:
                return -1

            heapq.heappush(max_heap, -fuel)
            prev_position = position
        
        return num_stops
