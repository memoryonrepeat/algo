# https://leetcode.com/problems/find-the-celebrity/

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        result = -1
        while candidate < n:
            others = [i for i in range(0, n) if i != candidate]
            print(candidate, others)
            isCeleb = True
            for o in others:
                if knows(candidate, o) == 1:
                    isCeleb = False
                    break
            if isCeleb == False:
                candidate += 1
                continue
            else:
                result = candidate
                break
        if result != -1:
            for i in [i for i in range(0, n) if i != result]:
                if knows(i, result) == 0:
                    return -1
        return result
        
                
                
                    
        
        