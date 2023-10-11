# https://leetcode.com/problems/number-of-flowers-in-full-bloom/
import bisect

# Using binary search to find the right place, true but TLE
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        sortedByStart = sorted(flowers, key = lambda f: f[0])
        result = []
        for p in people:
            left = bisect.bisect_right(list(map(lambda f: f[0], sortedByStart)), p)
            right = left - bisect.bisect_left(list(map(lambda f: f[1], sorted(sortedByStart[:left], key = lambda f: f[1]))), p)
            result.append(min(left,right))
        return result
