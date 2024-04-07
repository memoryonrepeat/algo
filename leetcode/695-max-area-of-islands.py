class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxArea = 0
        visited = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(i,j):
            if grid[i][j] == 0:
                return 0
            current = 1
            grid[i][j] = 0
            for dx,dy in directions:
                if 0<=i+dx<m and 0<=j+dy<n:
                    current += dfs(i+dx,j+dy)
            return current

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i,j))

        return maxArea
