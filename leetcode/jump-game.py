#https://leetcode.com/problems/jump-game/
class Solution:
    def canJumpFrom(self, nums: List[int], start, memoization) -> bool:
        if start == len(nums) - 1:
            return True
        for i in range(nums[start]):
            if start+i+1 >= len(nums):
                memoization[(start, i+1)] = False
                return False
            if (start,i+1) in memoization:
                return memoization[(start, i+1)]
            else:
                result = self.canJumpFrom(nums, start+i+1, memoization)
                memoization[(start, i+1)] = result
                if result == True:
                    return True
        return False
    
    def canJump(self, nums: List[int]) -> bool:
        memoization = {}
        return self.canJumpFrom(nums, 0, memoization)    
