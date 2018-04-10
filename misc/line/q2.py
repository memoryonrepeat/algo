class Node:
	
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

	def getValue(self):
		return self.value

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def getChildren(self):
		children = []
		if self.left:
			children.append(self.left)
		if self.right:
			children.append(self.right)
		return children

tree = Node('A', Node('B', Node('D', Node('G', None, None), None), None), Node('C', Node('E', None, None), Node('F', Node('H', None, None), Node('I', None, None))))

# This tree looks like this
#          A
#         / \
#        B   C
#       /   / \
#      D   E   F
#     /       / \
#    G       H   I
# 
# Correct answer should be A B C D E F G H I

# Using a strategy similar to bread-first search
# For new child nodes, store them to a queue
# By using queue (first in first out), nodes at the same depth are guaranteed to come out together
def traverse(node):
	fringe = [node]
	while (fringe):
		current_node = fringe.pop(0) # First in first out
		print(current_node.getValue())
		for child in current_node.getChildren():
			fringe.append(child)

traverse(tree)
