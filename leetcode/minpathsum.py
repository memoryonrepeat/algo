# https://leetcode.com/problems/minimum-path-sum/submissions/
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