# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        result = 0
        
        def getDepth(root):
            if not root:
                return 0
            nonlocal result
            leftDepth = getDepth(root.left)
            rightDepth = getDepth(root.right)
            result = max(result, leftDepth + rightDepth)
            return max(leftDepth, rightDepth) + 1
            
        getDepth(root)
        
        return result