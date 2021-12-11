# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        # Max money robbed if house i is the last house robbed
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0],nums[1])
            return nums[i]+max([dp(j) for j in range(i-1)])
            
        return max([dp(i) for i in range(len(nums))])

# Solution 2, only need to call dp twice to cover all odd /even houses
class Solution:
    result = 0
    
    def rob(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        # Max money robbed if house i is the last house robbed
        def dp(i):
            if i<0:
                temp = 0
            elif i == 0:
                temp = nums[0]
            elif i == 1:
                temp = max(nums[0],nums[1])
            else:
                temp = nums[i]+max([dp(j) for j in range(i-1)])
            self.result = max(self.result, temp)
            return temp
        
        dp(len(nums)-1)
        dp(len(nums)-2)
            
        return self.result