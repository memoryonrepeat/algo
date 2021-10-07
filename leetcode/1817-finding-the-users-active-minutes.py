# https://leetcode.com/problems/finding-the-users-active-minutes/

from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        counter = defaultdict(set)
        
        for user, time in logs:
            counter[user].add(time)
            
        result = [0 for _ in range(k)]
            
        for user in counter:
            uam = len(counter[user])
            result[uam-1] += 1
            
        return result
            
        