# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/submissions/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp_table = [[-1 for j in range(0, cols)] for i in range(0, rows)]
        result = 0
        for i in range(0, rows):
            for j in range(0, cols):
                result = max(result, self.dp(matrix, i, j, dp_table))
        return result
    
    def dp(self, matrix, i, j, dp_table):
        if dp_table[i][j] > -1:
            return dp_table[i][j]
        res = 1
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if (di*di + dj*dj == 1): # non-diagonal neighbors
                    next_i = i+di
                    next_j = j+dj
                    if next_i < 0 or next_j < 0 or next_i >= len(matrix) or next_j >= len(matrix[0]):
                        continue
                    if matrix[next_i][next_j] > matrix[i][j]:
                        res = max(res, 1 + self.dp(matrix, next_i, next_j, dp_table))
        dp_table[i][j] = res
        return res
        
# Redo 1/3/2024
# Using same backtrack technique as LC79, adding memoization to optimize
class Solution:
    def __init__(self):
        self.ans = 1
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        seen = {}
                
        def backtrack(i,j):               
            if (i,j) in seen:
                return seen[(i,j)]
            
            bestMove = 1
            
            for dx,dy in directions:
                if 0<=i+dx<m and 0<=j+dy<n and matrix[i][j] < matrix[i+dx][j+dy]:
                    bestMove = max(bestMove, 1 + backtrack(i+dx,j+dy))
                    
            seen[(i,j)] = bestMove
                    
            return seen[(i,j)]
            
        for i in range(m):
            for j in range(n):
                self.ans = max(self.ans, backtrack(i,j))
        
        return self.ans        