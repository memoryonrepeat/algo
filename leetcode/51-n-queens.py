# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = [["." for _ in range(n)] for _ in range(n)]
        
        def isSafe(row, col, cols, diagonals, antiDiagonals):
            return col not in cols and (row-col) not in diagonals and (row+col) not in antiDiagonals
        
        def solve(row, cols, diagonals, antiDiagonals, state):
            if row >= n:
                # NOTE: Need to clone since current state will be reset when backtracking
                solutions.append(["".join(row) for row in state])
                return
            
            for col in range(n):
                if isSafe(row, col, cols, diagonals, antiDiagonals):
                    state[row][col] = "Q"
                    cols.add(col)
                    diagonals.add(row-col)
                    antiDiagonals.add(row+col)
                                        
                    solve(row+1, cols, diagonals, antiDiagonals, state)
                    
                    # backtrack
                    state[row][col] = "."
                    cols.remove(col)
                    diagonals.remove(row-col)
                    antiDiagonals.remove(row+col)
                                        
        solve(0, set(), set(), set(), state)
        
        return solutions
                    
                        
        