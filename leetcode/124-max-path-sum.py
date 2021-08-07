# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.result = float('-inf')
    
    # Find max path that goes through the given node
    def dfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        # Final result has to consider paths that goes through one of these possibilities:
        # - root only
        # - Max path through left child + root
        # - Max path through right child + root
        # - Max path through left child + Max path through right child + root
        self.result = max(self.result, root.val, max(left,right) + root.val, left + right + root.val)
        
        # For each recursive call through non-root nodes, the potential path can only goes through
        # either left child or right child, or that root itself (in case both left and right branches yields negative sum).
        # Note that in case both left and right branches yield positive sums and node is negative itself, this non-optimal
        # result that goes through the current negative node and whatever left/right sum may be temporarily accepted 
        # but in the end it will still fall behind left or right sum due to the global comparison againts self.result above.
        return max(max(left,right) + root.val, root.val)
    
    def maxPathSum(self, root):
        self.dfs(root)
        return self.result
        