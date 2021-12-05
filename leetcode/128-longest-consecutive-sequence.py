# https://leetcode.com/problems/longest-consecutive-sequence/

from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        c = Counter(nums)
        longest = 1
        for num in nums:
            original = num
            # print(num, c, longest)
            if num not in c:
                continue
            localMax = 1
            while num-1 in c:
                del c[num-1]
                num -= 1
                localMax += 1
            num = original
            while num+1 in c:
                del c[num+1]
                num += 1
                localMax += 1
            longest = max(longest, localMax)
            
        return longest
            