# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    nodes = defaultdict(list)
    
    def traverse(self, root, column, row):
        if root:
            self.nodes[column].append((root.val, row))
            self.nodes[column].sort(key = lambda x: x[1])
            if root.left:
                self.traverse(root.left, column-1, row+1)
            if root.right:
                self.traverse(root.right, column+1, row+1)
    
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        self.nodes = defaultdict(list)
        self.traverse(root, 0, 0)
                
        return map(lambda x: map(lambda y: y[0], x), (self.nodes[key] for key in sorted(self.nodes.keys())))