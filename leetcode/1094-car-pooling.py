# https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tasks = []
        
        for passengers,start,end in trips:
            tasks.append((start,passengers))
            tasks.append((end,-passengers))
            
        tasks.sort()
        
        for task in tasks:
            capacity -= task[1]
            if capacity < 0:
                return False
            
        return True
        