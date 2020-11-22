# https://leetcode.com/problems/number-of-islands/submissions/
class Solution:
    def dfs(self, i, j, grid):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(i-1,j,grid)
        self.dfs(i+1,j,grid)
        self.dfs(i,j-1,grid)
        self.dfs(i,j+1,grid)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island_count += 1
                    self.dfs(i,j,grid)
        return island_count