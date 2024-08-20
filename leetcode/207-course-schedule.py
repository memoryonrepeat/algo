from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMatrix = defaultdict(list)

        for a,b in prerequisites:
            adjMatrix[a].append(b)

        def dfs(start, visited):
            nonlocal adjMatrix
            if start in visited:
                return False
            for prereqs in adjMatrix[start]:
                if not dfs(prereqs, visited + [start]):
                    return False
            return True

        for i in list(adjMatrix):
            if not dfs(i, []):
                return False

        return True
