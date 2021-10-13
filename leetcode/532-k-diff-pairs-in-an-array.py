# https://leetcode.com/problems/k-diff-pairs-in-an-array/

from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        c = Counter(nums)
        for num in c.keys():
            if k==0:
                if c[num] > 1:
                    result += 1
            else:
                if num+k in c:
                    result += 1
        return result