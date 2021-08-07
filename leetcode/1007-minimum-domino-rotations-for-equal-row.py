# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        topsCount = {k: 0 for k in range(0, 7)}
        bottomsCount = {k: 0 for k in range(0, 7)}
        sameCount = {k: 0 for k in range(0, 7)}
        length = len(tops)
        for i in range(length):
            if tops[i] == bottoms[i]:
                sameCount[tops[i]] += 1
            topsCount[tops[i]] += 1
            bottomsCount[bottoms[i]] += 1
        ans = length+1
        # print(topsCount, bottomsCount, sameCount)
        for i in range(0,7):
            if topsCount[i] + bottomsCount[i] - sameCount[i] >= length:
                ans = min(ans, length - max(topsCount[i], bottomsCount[i]))
            
        if ans == length+1:
            return -1
        
        return ans
            
            
        
        
        