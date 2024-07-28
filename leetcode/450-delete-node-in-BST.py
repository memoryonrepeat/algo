# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addNode(self, root, node):
        if not root:
            return node
        if root.val < node.val:
            root.right = self.addNode(root.right, node)
        else:
            root.left = self.addNode(root.left, node)
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left:
                leftNode = root.left
                root = root.right
                root = self.addNode(root, leftNode)
            else:
                root = root.right
        return root