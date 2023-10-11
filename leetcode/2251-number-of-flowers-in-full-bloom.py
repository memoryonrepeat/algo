# https://leetcode.com/problems/number-of-flowers-in-full-bloom/

# Use single array for binary search --> AC
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        sortedByStart = sorted(list(map(lambda f: f[0], flowers)))
        sortedByEnd = sorted(list(map(lambda f: f[1]+1, flowers)))
        result = []
        for p in people:
            started_blooming = bisect_right(sortedByStart, p)
            ended_blooming = bisect_right(sortedByEnd, p)
            result.append(started_blooming - ended_blooming)
        return result

# Initial solution, same idea but TLE
class _Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        sortedByStart = sorted(flowers, key = lambda f: f[0])
        result = []
        for p in people:
            left = bisect.bisect_right(list(map(lambda f: f[0], sortedByStart)), p)
            right = left - bisect.bisect_left(list(map(lambda f: f[1], sorted(sortedByStart[:left], key = lambda f: f[1]))), p)
            result.append(min(left,right))
        return result