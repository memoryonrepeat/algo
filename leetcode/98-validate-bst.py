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
            if node.val >= high:
                return False
            if node.val <= low:
                return False
            if node.left:
                isValidLeft = isValid(node.left, min(node.val, high), low)
                if not isValidLeft:
                    return False
            if node.right:
                isValidRight = isValid(node.right, high, max(node.val, low))
                if not isValidRight:
                    return False
            return True

        return isValid(root, math.inf, -math.inf)