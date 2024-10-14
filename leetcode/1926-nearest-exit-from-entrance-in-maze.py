from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        moves = [(0,1), (0,-1), (-1,0), (1,0)]
        m = len(maze)
        n = len(maze[0])
        visited = []
        candidates = deque([[entrance[0], entrance[1], 0]])

        def isBound(x,y):
            return maze[x][y] == "." and (x==0 or x==m-1 or y==0 or y==n-1) and [x,y] != entrance

        def isValid(x,y):
            return 0<=x<m and 0<=y<n and maze[x][y] == "."

        while candidates:
            [x,y,d] = candidates.popleft()
            if isBound(x,y):
                return d
            if [x,y] in visited:
                continue
            visited.append([x,y])
            neighbors = [[x+dx, y+dy] for (dx,dy) in moves if isValid(x+dx, y+dy)]
            candidates += [(x,y,d+1) for [x,y] in neighbors if [x,y] not in visited]

        return -1
