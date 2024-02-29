class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
                
        def backtrack(i,j,target,visited):
            if not target:
                return False
            if board[i][j] != target[0]:
                return False
            if board[i][j] == target:
                return True
            
            for dx,dy in directions:
                if 0<=i+dx<m and 0<=j+dy<n and (i+dx,j+dy) not in visited and backtrack(i+dx,j+dy,target[1:],visited + [(i,j)]):
                    return True
                
            return False
            
        for i in range(m):
            for j in range(n):
                if backtrack(i,j,word,[]):
                    return True
        
        return False
        