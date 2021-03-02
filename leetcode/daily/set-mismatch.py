# https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # The full set of numbers from 1 to n without duplicate
        full = set(range(1,len(nums)+1))
        
        # The missing number
        missing = list(full - set(nums))[0]
        
        # Add missing num to both original list and full list
        # The difference between both sums are the duplicate
        nums.append(missing)
        full.add(missing)
        
        return [sum(nums)-sum(full), missing]