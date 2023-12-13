# https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def dp(x,y):
            if x>=m or y>=n:
                return 0
            if x==m-1:
                if y==n-1:
                    return 1
                return dp(x,y+1)
            if y==n-1:
                return dp(x+1,y)
            
            return dp(x+1,y)+dp(x,y+1)

        return dp(0,0)