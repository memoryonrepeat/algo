# https://leetcode.com/problems/minimum-knight-moves/

from collections import deque

class Solution:
    # Basic bfs without restricting search space to first quadrant
    def bfs_basic(self, x: int, y: int) -> int:
        moves = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (-1, 2), (1,-2), (1,2)]
        queue = deque([((0,0), 0)])
        visited = set((0,0))
        while queue: # queue is not empty
            current, dist = queue.popleft()
            if current[0] == x and current[1] == y:
                return dist
            possibleMoves = map(lambda move: (current[0] + move[0], current[1] + move[1]), moves)
            for possibleMove in possibleMoves:
                if possibleMove not in visited: # to avoid loop
                    queue.append((possibleMove, dist+1))
                    visited.add(possibleMove)
    
    # Optimized bfs, only search within first quadrant thanks to symmetry
    def bfs_optimized(self, x: int, y: int) -> int:
        moves = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (-1, 2), (1,-2), (1,2)]
        queue = deque([((0,0), 0)])
        visited = set((0,0))
        while queue: # queue is not empty
            current, dist = queue.popleft()
            if current[0] == x and current[1] == y:
                return dist
            possibleMoves = map(lambda move: (current[0] + move[0], current[1] + move[1]), moves)
            for possibleMove in possibleMoves:
                if possibleMove not in visited: # to avoid loop
                    if possibleMove[0]>=-2 and possibleMove[0]>=-2: # possibleMove must be within first quadrant
                        queue.append((possibleMove, dist+1))
                        visited.add(possibleMove)
        
    def minKnightMoves(self, x: int, y: int) -> int:
        return self.bfs_optimized(abs(x), abs(y))
        # return self.bfs_basic(x,y)