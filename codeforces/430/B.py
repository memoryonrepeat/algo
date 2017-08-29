import math
R,d = [int(x) for x in input().split()]
rs = R-d
n = int(input())
arr = []
for i in range(n):
	arr.append([int(x) for x in input().split()])

def main(sausages):
	count = 0
	for sausage in sausages:
		x,y,r = sausage[0],sausage[1],sausage[2]
		if x*x+y*y>=(rs+r)*(rs+r) and x*x+y*y<=(R-r)*(R-r):
			count += 1
	return count

print(main(arr))