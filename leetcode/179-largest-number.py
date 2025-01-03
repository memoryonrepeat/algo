# https://leetcode.com/problems/largest-number/

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ordered = sorted(nums, key = cmp_to_key(lambda x,y: 1 if (str(x)+str(y) < str(y)+str(x)) else -1))
        return "0" if ordered[0]==0 else ''.join(map(str,ordered))