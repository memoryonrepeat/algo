from collections import defaultdict
# https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        def isSimilar(s1, s2):
            differences = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    differences += 1
            return differences == 2
        
        def buildGraph(strs):
            graph = defaultdict(set)
            for s1 in strs:
                for s2 in strs:
                    if isSimilar(s1, s2):
                        graph[s1].add(s2)
                        graph[s2].add(s1)
            return graph
        
        graph = buildGraph(strs)
        
        # print(graph)
        
        def dfs(node, result):
            result.add(node)
            if node not in graph:
                return result
            for neighbor in graph[node]:
                if neighbor not in result:
                    result.update(dfs(neighbor, result))
            return result
        
        groups = 0
        
        strSet = set(strs)
        
        while len(strSet)>0:
            groups += 1
            current = dfs(strSet.pop(), set([]))
            # print(current)
            strSet -= current
            
        return groups