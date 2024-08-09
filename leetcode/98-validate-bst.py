# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, high, low):
            if not node:
                return True
            if node.val >= high or node.val <= low:
                return False
            return isValid(node.left, node.val, low) and isValid(node.right, high, node.val)

        return isValid(root, math.inf, -math.inf)