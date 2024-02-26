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

# Redo 26/2/24
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        m = len(grid)
        n = len(grid[0])
        visited = set()
        
        def dfs(i,j):
            visited.add((i,j))
            grid[i][j] = "0"
            for dx,dy in directions:
                r,c = i+dx,j+dy
                if 0<=r<m and 0<=c<n and (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
            
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == "1":
                    numIslands +=1
                    dfs(i,j)
        
        return numIslands