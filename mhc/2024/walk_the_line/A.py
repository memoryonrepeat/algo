# https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/A

import math

f = open("walk_the_line_input.txt", "r")

T = int(f.readline())
result = []

def solve(group, k):
	if len(group) == 1:
		if k >= group[0]:
			result.append("YES")
			return
		result.append("NO")
		return
	fastest = min(group)
	if k >= (2*fastest*(len(group)-2) + fastest):
		result.append("YES")
		return
	result.append("NO")

for _ in range(T):
	n,k = map(int, f.readline().split(" "))
	group = []
	for _ in range(n):
		group.append(int(f.readline()))
	solve(group, k)

print("\n".join(["Case #{i}: {r}".format(i=i+1,r=result[i]) for i in range(len(result))]))