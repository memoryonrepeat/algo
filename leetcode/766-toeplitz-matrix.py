# https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        topDiagonals = [ [matrix[i][i+j] for i in range(m) if i+j<n] for j in range(n) ]
        bottomDiagonals = [ [matrix[i+j][i] for i in range(n) if i+j<m] for j in range(m) ]
        
        return all(all(e == d[0] for e in d) for d in topDiagonals + bottomDiagonals)