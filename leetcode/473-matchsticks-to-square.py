# https://leetcode.com/problems/matchsticks-to-square/

from collections import Counter
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sideLength = sum(matchsticks)
        if sideLength % 4 != 0:
            return False
        sideLength = sideLength // 4
        matchsticks.sort(reverse=True)
        sides = [0,0,0,0]
        
        def backtrack(index):
            if index == len(matchsticks):
                if sides[0] == sides[1] == sides[3] == sideLength:
                    return True
                return False
            for i in range(4):
                if matchsticks[index] + sides[i] <= sideLength:
                    sides[i] += matchsticks[index]
                    if backtrack(index+1) == True:
                        return True
                    sides[i] -= matchsticks[index]
            return False
                
            
        return backtrack(0)
        