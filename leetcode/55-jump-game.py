# https://leetcode.com/problems/jump-game/

from functools import lru_cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        @lru_cache(maxsize=None)
        def dp(i):
            if i == len(nums)-1:
                return True
            for j in range(i+1,min(len(nums), i+nums[i]+1)):
                if dp(j):
                    return True
            return False
        
        return dp(0)