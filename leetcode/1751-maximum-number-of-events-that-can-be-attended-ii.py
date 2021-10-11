# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

# Idea:
# Sort events by start day
# Loop through each event, consider whether to attend or not
# Similar to knapsack

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [e[0] for e in events]
        
        @lru_cache(maxsize=None)
        def dp(i, k):
            if k==0 or i>=len(events):
                return 0
            next_day = bisect_right(starts, events[i][1])
            return max(dp(i+1, k), dp(next_day,k-1) + events[i][2])
            
        return dp(0,k)