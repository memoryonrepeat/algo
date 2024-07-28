from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjMatrix = defaultdict(list)

        for e,v in zip(equations, values):
            adjMatrix[e[0]].append((e[1], v))
            adjMatrix[e[1]].append((e[0], 1/v))
            adjMatrix[e[0]].append((e[0], 1))

        def dfs(start, end, visited, total):
            visited.add(start)
            neighbors = adjMatrix[start]
            if not neighbors:
                return -1
            for neighbor, division in neighbors:
                if neighbor == end:
                    return total * division
                if neighbor in visited:
                    continue
                result = dfs(neighbor, end, visited, total * division)
                if result > -1:
                    return result
            return -1

        result = []

        for query in queries:
            result.append(dfs(query[0], query[1], set(), 1))

        return result