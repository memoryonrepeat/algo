# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

# Key observation: 
# Increasing n-1 elements by 1 is equivalent to decreasing 1 element by 1
# Since we are only concerned with relativity between numbers
# -> In the end it's equal to decreasing all elements to smallest element

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums)*len(nums)