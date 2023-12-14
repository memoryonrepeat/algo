# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def dfs(self, sourceX, sourceY, targetX, targetY, grid, mem):
        if sourceX>=len(grid) or sourceY>=len(grid[0]):
            return float("inf")
        if sourceX == targetX and sourceY == targetY:
            return grid[targetX][targetY]
        if (sourceX, sourceY) in mem:
            return mem[(sourceX, sourceY)]
        global_min = float("inf")
        neighbors = [(sourceX+1, sourceY), (sourceX, sourceY+1)]
        for neighbor in neighbors:
            global_min = min(global_min, grid[sourceX][sourceY] + self.dfs(neighbor[0], neighbor[1], targetX, targetY, grid, mem))
        mem[(sourceX, sourceY)] = global_min
        return global_min
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.dfs(0,0,len(grid)-1,len(grid[0])-1, grid, {})

# More concise solution - 2023
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0)]
        m = len(grid)
        n = len(grid[0])

        @lru_cache(maxsize=None)
        def dp(x,y):
            if x>=m or y>=n:
                return 200*200
            if x==m-1 and y==n-1:
                return grid[x][y]
            return min(list(map(lambda d: grid[x][y] + dp(x+d[0], y+d[1]) , directions)))

        return dp(0,0)