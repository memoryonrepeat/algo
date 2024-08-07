# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(deque)
        
        def traverse(node, level):
            if not node:
                return
            
            if level % 2 == 0:
                result[level].append(node.val)
            else:
                result[level].appendleft(node.val)
            
            if node.left:
                traverse(node.left, level+1)
            if node.right:
                traverse(node.right, level+1)
                
        traverse(root, 0)
        
        return result.values()