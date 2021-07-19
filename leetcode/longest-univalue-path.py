# https://leetcode.com/problems/longest-univalue-path/submissions/

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        
        
        self.longest = 0
        self.get_uniValuePath(root)
        return self.longest
    
    def get_uniValuePath(self, node):
        
        if not node:
            return None, 0
        
        if not node.left and not node.right:
            return node.val, 1
        
        left, count_L = self.get_uniValuePath(node.left)
        right, count_R = self.get_uniValuePath(node.right)
        
        if left == node.val and right == node.val:
            self.longest = max(self.longest, count_L + count_R)
            return node.val, max(count_L, count_R) + 1
        
        if left == node.val:
            self.longest = max(self.longest, count_L)
            return node.val, count_L + 1
        
        if right == node.val:
            self.longest = max(self.longest, count_R)
            return node.val, count_R + 1
        
        return node.val, 1