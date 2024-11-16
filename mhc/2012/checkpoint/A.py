# https://www.facebook.com/codingcompetitions/hacker-cup/2012/round-1/problems/A

import math

f = open("checkpoint_input.txt", "r")

R = int(f.readline())

cases = [int(f.readline()) for _ in range(R)]

result = []

table = {}

# Let C(s,a) = ways to select a elements from s elements
# C(s,a) = s!/(a!*(s-a)!) = (s-a+1)*(s-a+2)*...*s/a!
# table will map C(s,a) to s
def populateTable():
	for i in range(10000000,0,-1):
		comb = 1
		for j in range(1,i+1):
			comb *= i-j+1
			comb //= j
			if comb > 10000000:
				break
			table[comb] = i
# Idea:
# Let C(a,b) = ways to select b elements from a elements
# Then S = C(x1+y1, x1) * C(x2+y2,x2) 
# where (x1,y1) is checkpoint and (x2,y2) is absolute distance between target and checkpoint
# And T = x1+y1+x2+y2 (Manhattan distance)
# Find all integer pairs that multiply to S --> Precalculate to get which (x,y) pairs yields those numbers
def solve():
	for s in cases:
		t = float("inf")
		for a in range(1, math.ceil(math.sqrt(s)+1)):
			if s%a == 0:
				t = min(t, table[a] + table[s//a])
		result.append(t)

populateTable()
solve()
print("\n".join(["Case #{i}: {r}".format(i=i+1,r=result[i]) for i in range(len(result))]))