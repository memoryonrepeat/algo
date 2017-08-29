import math

l,r,x,y,k = [int(x) for x in input().split()]

if math.ceil(l/y)<=k and k<=math.floor(r/x):
	print("YES")
else:
	print("NO")