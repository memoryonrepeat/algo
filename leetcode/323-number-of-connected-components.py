# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMatrix = defaultdict(list)
        
        remaining = [i for i in range(n)]
        
        for a,b in edges:
            adjMatrix[a].append(b)
            adjMatrix[b].append(a)
        
        components = 0
        
        # print(adjMatrix)
        
        def dfs(s: str):
            remaining.remove(s)
            
            for neighbor in adjMatrix[s]:
                if neighbor in remaining:
                    dfs(neighbor)
                    
        while remaining:
            seed = remaining[0]
            components += 1
            dfs(seed)
            # print(remaining)
            
        return components