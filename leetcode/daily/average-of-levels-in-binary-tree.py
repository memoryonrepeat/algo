# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root, depth, result):
        try:
            result[depth][0] += root.val
            result[depth][1] += 1
        except IndexError:
            result.append([root.val, 1])
        if root.left:
            self.bfs(root.left, depth+1, result)
        if root.right:
            self.bfs(root.right, depth+1, result)
        
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        self.bfs(root, 0, result)
        return map(lambda x: x[0]/x[1], result)