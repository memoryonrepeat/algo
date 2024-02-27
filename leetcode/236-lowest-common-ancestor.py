# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(current):
            if not current:
                return False
            
            left = dfs(current.left)
            right = dfs(current.right)
            mid = (current.val == p.val) or (current.val == q.val)
            
            if left+right+mid >= 2:
                self.ans = current
            
            return mid or left or right
                
        dfs(root)
        
        return self.ans