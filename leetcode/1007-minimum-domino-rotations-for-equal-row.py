# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # A solution exists for a number k when the total amount of k at different indexes
        # in both tops and bottoms are bigger or equal to length of tops / bottoms.
        # In such case, just switch all dominos at whichever row has smaller amount of k

        # Therefore, we maintain a counter for both tops and bottoms, also a counter
        # when same number appear at same index, to avoid double counting for same indexes

        topsCount = {k: 0 for k in range(0, 7)}
        bottomsCount = {k: 0 for k in range(0, 7)}
        sameCount = {k: 0 for k in range(0, 7)}

        length = len(tops)

        # Initiate the counters
        for i in range(length):
            if tops[i] == bottoms[i]:
                sameCount[tops[i]] += 1
            topsCount[tops[i]] += 1
            bottomsCount[bottoms[i]] += 1

        ans = length+1
        
        # Go through all potential solutions and update global minima
        # Note that we need to minus sameCount to avoid double counting those at the same indexes
        for i in range(0,7):
            if topsCount[i] + bottomsCount[i] - sameCount[i] >= length:
                ans = min(ans, length - max(topsCount[i], bottomsCount[i]))
            
        if ans == length+1:
            return -1
        
        return ans
            
            
        
        
        