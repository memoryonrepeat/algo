from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        gates = []

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    gates.append((i,j))

        def isValid(x,y):
            return 0<=x<m and 0<=y<n and rooms[x][y]>0

        def bfs(i,j):
            visited = []
            candidates = deque([[i,j,0]])

            while candidates:
                x,y,d = candidates.popleft()
                rooms[x][y] = min(rooms[x][y],d)
                visited.append([x,y])
                neighbors = [[x+dx,y+dy] for dx,dy in moves if isValid(x+dx,y+dy)]
                candidates += [[nx,ny,d+1] for nx,ny in neighbors if [nx,ny] not in visited]
                
        for i,j in gates:
            bfs(i,j)

