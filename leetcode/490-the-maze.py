class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m,n = len(maze), len(maze[0])
                
        def isWall(x,y):
            return x<0 or y<0 or x>=m or y>=n or maze[x][y] == 1
        
        def stopAt(s, d):
            tempS = s[:]
            while not isWall(tempS[0], tempS[1]):
                tempS[0] += d[0]
                tempS[1] += d[1]
            return [tempS[0] - d[0], tempS[1] - d[1]]
        
        def getNeighbors(s):
            directions = [[-1,0], [1,0], [0,-1], [0,1]]
            result = []
            for d in directions:
                nextStop = stopAt(s,d)
                if nextStop != s:
                    result += [nextStop]
            return result
        
        def dfs(s, visited):
            if s == destination:
                return True
            visited += [s]
            for neighbor in getNeighbors(s):
                if neighbor not in visited and dfs(neighbor, visited):
                    return True
            return False
            
        return dfs(start, [])