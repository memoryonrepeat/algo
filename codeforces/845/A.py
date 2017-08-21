n = int(input())
arr = []

arr = [int(x) for x in input().split()]

arr.sort()

if (arr[n]==arr[n-1]):
	print("NO")
else:
	print("YES")