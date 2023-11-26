class Solution:
    def __init__(self):
        self.adjMatrix = defaultdict(list)
        self.visited = set()
        self.provinces = 0

    def buildAdjMatrix(self, isConnected):
        for i, row in enumerate(isConnected):
            self.adjMatrix[i] = []
            for j, col in enumerate(row):
                if col == 1:
                    self.adjMatrix[i].append(j)

    def dfs(self, current, isNewProvince):
        if current in self.visited:
            return
        if isNewProvince:
            self.provinces += 1
        self.visited.add(current)
        neighbors = self.adjMatrix[current]
        while neighbors:
            neighbor = neighbors.pop()
            self.dfs(neighbor, False)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.buildAdjMatrix(isConnected)
        for i in self.adjMatrix:
            self.dfs(i, True)
        return self.provinces