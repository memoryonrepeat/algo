# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def getHeight(self, root):
        if not root:
            return 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        if (left_height == -1 or right_height == -1 or abs(left_height - right_height)>1):
            return -1
        return max(left_height, right_height)+1
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.getHeight(root)!=-1
        
        