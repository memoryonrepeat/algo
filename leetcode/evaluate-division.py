# https://leetcode.com/problems/evaluate-division/
class Solution:
	def __init__(self):
		self.graph = {}

	def build_graph(self, equations, values):
		for i, (source, target) in enumerate(equations):
			self.add_to_graph(source, target, values[i])
			self.add_to_graph(target, source, 1/values[i])

	def add_to_graph(self, source, target, value):
		if source not in self.graph:
			self.graph[source] = [(target, value)]
		else:
			self.graph[source].append((target, value))
	
	def calculate(self, query, visited):
		source = query[0]
		target = query[1]
		if source not in self.graph or target not in self.graph:
			return -1
		visited.append(source)
		if len(self.graph[source]) == 1 and self.graph[source][0][0] == target:
			return self.graph[source][0][1]
		for neighbor,value in self.graph[source]:
			if neighbor == target:
				return value
			if neighbor not in visited:
				current_res = self.calculate([neighbor, target], visited)
				if current_res > 0:
					return value * current_res
		return -1
	
	def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
		result = []
		self.build_graph(equations, values)
		for query in queries:
			result.append(self.calculate(query, []))
		return result
