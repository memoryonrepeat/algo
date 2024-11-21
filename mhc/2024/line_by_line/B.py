# https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/A

import math

f = open("line_by_line_input.txt", "r")

T = int(f.readline())
result = []

def solve(n, p):
	result.append(100 * (math.pow(p,(n-1)/n) - p))

for _ in range(T):
	n,p = map(int, f.readline().split(" "))
	solve(n, p/100)

print("\n".join(["Case #{i}: {r}".format(i=i+1,r=result[i]) for i in range(len(result))]))