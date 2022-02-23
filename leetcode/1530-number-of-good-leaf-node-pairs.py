# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

class Solution:
    
    def countPairs(self, root: TreeNode, distance: int) -> int:
        result = 0
        
        def scan(root):
            nonlocal result
            
            if not root:
                return []
            if not root.left and not root.right:
                return [1]
            
            left = scan(root.left)
            right = scan(root.right)
            
            # print(root.val, left, right)
            
            result += len([l+r for l in left for r in right if l+r <= distance])
            
            return [d+1 for d in left+right if d+1 <= distance]
            
        scan(root)
        
        return result
        