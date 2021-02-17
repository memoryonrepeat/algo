# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
from collections import defaultdict 

class Solution:
    graph = defaultdict(list)
    
    def generateGraph(self, root):
        self.graph = defaultdict(list)

        neighbors = [root]
        
        while neighbors:
            current = neighbors.pop()
            # self.graph[current.val] = []
            if current.left:
                neighbors.append(current.left)
                self.graph[current.val].append(current.left.val)
                self.graph[current.left.val].append(current.val)
            if current.right:
                neighbors.append(current.right)
                self.graph[current.val].append(current.right.val)
                self.graph[current.right.val].append(current.val)
    
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        self.generateGraph(root)
        
        q = deque([k])
        seen = set()
                
        while q:
            current = q.popleft()
            seen.add(current)
            if len(self.graph[current]) <= 1 and current != root.val:
                return current
            for neighbor in self.graph[current]:
                if neighbor not in seen:
                    q.append(neighbor)
        
        return root.val
                    
                    
                
                
        