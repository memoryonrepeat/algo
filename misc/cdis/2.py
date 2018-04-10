class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    
# Traverse in a DFS manner    
def serialize_tree_dfs(tree):
	if not tree:
		return [None]
	if not tree.left and not tree.right:
		return [tree.val]
	return [tree.val] + serialize_tree_dfs(tree.left) + serialize_tree_dfs(tree.right)

# Traverse in a BFS manner
def serialize_tree_bfs(tree):
	if not tree:
		return [None]
	result = []
	queue = Queue()
	queue.enqueue(tree)
	while not queue.isEmpty():
		current = queue.dequeue()
		if current:
			if current.left or current.right:
				queue.enqueue(current.left)
				queue.enqueue(current.right)
			result.append(current.val)
		else:
			result.append(None)
	return result
    
tree = Node(1, Node(2, None, Node(4, None, None)), Node(3, Node(2, None, None), None))
assert serialize_tree_bfs(tree)==[1,2,3,None,4,2,None], serialize_tree_bfs(tree)
assert serialize_tree_dfs(tree)==[1,2,None,4,3,2,None], serialize_tree_dfs(tree)

