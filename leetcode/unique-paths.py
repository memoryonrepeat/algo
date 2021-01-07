# https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePathsFrom(self, m: int, n: int, startX,  startY, cache) -> int:
        if (startX, startY) in cache:
            return cache[(startX, startY)]
        if startX == m-1 and startY == n-1:
            cache[(startX, startY)] = 1
            return 1
        if startX > m-1 or startY > n-1:
            cache[(startX, startY)] = 0
            return 0
        downTotal = self.uniquePathsFrom(m,n,startX+1,startY, cache)
        cache[(startX+1, startY)] = downTotal
        rightTotal = self.uniquePathsFrom(m,n,startX,startY+1, cache)
        cache[(startX, startY+1)] = rightTotal
        return downTotal + rightTotal
    
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        return self.uniquePathsFrom(m,n,0,0,cache)
