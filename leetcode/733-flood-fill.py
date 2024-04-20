from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        same = image[sr][sc]
        m = len(image)
        n = len(image[0])

        def bfs(x,y):
            neighbors = deque([])
            image[x][y] = color
            visited.add((x,y))
            for dx,dy in directions:
                if 0<=x+dx<m and 0<=y+dy<n:
                    if image[x+dx][y+dy] == same and (x+dx,y+dy) not in visited:
                        neighbors.append([x+dx, y+dy])
            while neighbors:
                x,y = neighbors.popleft()
                bfs(x,y)

        bfs(sr, sc)
        return image