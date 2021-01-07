# https://leetcode.com/problems/closest-binary-search-tree-value/
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        result = root
        while root:
            result = min(root, result, key = lambda x: abs(x.val - target))
            root = root.left if target < root.val else root.right
        return result.val
