# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftBranch = []
        rightBranch = []
        
        def dfs(node, leftFirst, current):
            if not node:
                current.append(None)
                return
            current.append(node.val)
            if leftFirst:
                dfs(node.left, leftFirst, current)
                dfs(node.right, leftFirst, current)
            else:
                dfs(node.right, leftFirst, current)
                dfs(node.left, leftFirst, current)
            
        dfs(root.left, True, leftBranch)
        dfs(root.right, False, rightBranch)
        
        return leftBranch == rightBranch