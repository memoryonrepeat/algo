# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/binary-tree-level-order-traversal/

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        nodes = deque([(root, 0)])
        result = []
        while nodes:
            current, val = nodes.popleft()
            result.append((current.val,val))
            if current.left:
                nodes.append((current.left, val+1))
            if current.right:
                nodes.append((current.right, val+1))
        i = 0
        local_result = []
        global_result = []
        while i < len(result):
            current_val = result[i][1]
            while i < len(result) and result[i][1] == current_val:
                local_result.append(result[i][0])
                i += 1
            global_result.append(local_result)
            local_result = []
        return global_result