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
        return res
        