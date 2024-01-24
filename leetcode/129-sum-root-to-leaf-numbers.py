# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, current, total):
            if not root.left and not root.right:
                current += str(root.val)
                total += int(current)
                return total
            if root.left and not root.right:
                return dfs(root.left, current+str(root.val), total)
            if root.right and not root.left:
                return dfs(root.right, current+str(root.val), total)
            return dfs(root.left, current+str(root.val), total) + dfs(root.right, current+str(root.val), total)

        return dfs(root, "", 0)