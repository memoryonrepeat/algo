# https://leetcode.com/problems/unique-paths-ii/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @lru_cache(maxsize=None)
        def dp(x,y):
            if x>=m or y>=n or obstacleGrid[x][y] == 1:
                return 0
            if x==m-1:
                if y==n-1:
                    return 1
                return dp(x,y+1)
            if y==n-1:
                return dp(x+1,y)
            
            return dp(x+1,y)+dp(x,y+1)

        return dp(0,0)