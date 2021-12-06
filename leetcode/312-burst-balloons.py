# https://leetcode.com/problems/burst-balloons/

from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]
        
        @lru_cache(maxsize=None)
        def dp(start, end):
            if start > end:
                return 0
            result = 0
            for i in range(start, end+1):
                lastGain = nums[start-1] * nums[i] * nums[end+1]
                totalScore = dp(start,i-1) + lastGain + dp(i+1,end)
                result = max(result, totalScore)
            return result
            
        return dp(1,len(nums)-2)