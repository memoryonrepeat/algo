from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        time_passed = 0
        neighbors = deque([])
        fresh_oranges = 0

        def bfs():
            nonlocal time_passed
            nonlocal fresh_oranges
            
            while neighbors:
                x,y,prev = neighbors.popleft()

                if (x,y) in visited:
                    continue

                visited.add((x,y))

                if grid[x][y] != 2:
                    grid[x][y] = 2
                    time_passed = max(time_passed, prev+1)
                    fresh_oranges -= 1
                    if fresh_oranges == 0:
                        break

                for dx,dy in directions:
                    if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == 1:
                        neighbors.append([x+dx,y+dy,time_passed])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    neighbors.append([i,j,0])

        bfs()

        if fresh_oranges > 0:
            return -1
        
        return time_passed
