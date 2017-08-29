n,m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
queries = []
for i in range(m):
	queries.append(int(input()))

for query in queries:
	arr = [e^query for e in arr]
	arr.sort()
	minimum = 0
	i=0
	while (minimum==arr[i]):
		i += 1
		minimum += 1
		if i==len(arr):
			break
	print(minimum)