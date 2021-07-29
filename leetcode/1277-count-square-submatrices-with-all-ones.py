# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        result = 0
        
        # Reuse matrix as memoization table
        # dp[i][j] = number of all squares with (i,j) at bottom right
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i==0 or j==0:
                        result += 1
                    else:
                        matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                        result += matrix[i][j]
                    
        return result
        