# Brute force - TLE
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        deltas = [(-1,0),(1,0),(0,-1),(0,1)]

        def isValid(x,y):
            nonlocal m,n
            return 0 <= x < m and 0 <= y < n

        def dfs(x, y, effort, visited):
            if x == m-1 and y == n-1:
                return effort

            neighbors = [(x+dx, y+dy) for dx,dy in deltas if isValid(x+dx,y+dy)]
            result = 1000000
            for i,j in neighbors:
                if (i,j) not in visited:
                    result = min(result, dfs(i,j,max(effort, abs(heights[x][y] - heights[i][j])),visited + [(x,y)]))

            return result

        return dfs(0,0,0,[])

# Same but update visited outside dfs parameters
# Note that in this case, need to pass a copy of the updated visited instead of the original one
# Since visited is a list and will be passed by reference --> updates in search branches will be recorded when backtracking
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        deltas = [(-1,0),(1,0),(0,-1),(0,1)]

        def isValid(x,y):
            nonlocal m,n
            return 0 <= x < m and 0 <= y < n

        def dfs(x, y, effort, visited):
            if x == m-1 and y == n-1:
                # print(visited, effort)
                return effort
            visited.append((x,y))
            neighbors = [(x+dx, y+dy) for dx,dy in deltas if isValid(x+dx,y+dy)]
            result = 1000000
            for i,j in neighbors:
                if (i,j) not in visited:
                    result = min(result, dfs(i,j,max(effort, abs(heights[x][y] - heights[i][j])),visited[:]))

            return result

        return dfs(0,0,0,[])