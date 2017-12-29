# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.max_depth = 0
        
    def dfs(self, root, depth):
        if not root:
            return 0
        if root and not root.left and not root.right and depth > self.max_depth:
            self.max_depth = depth
            return depth
        return max(self.dfs(root.left, depth+1), self.dfs(root.right, depth+1))
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 1)
        