tic = input()
arr = [int(digit) for digit in tic]
arr1 = arr[:3]
arr2 = arr[3:]
sum1 = sum(arr1)
sum2 = sum(arr2)
turns1 = 0
turns2 = 0
if sum1>sum2:
	arr1.sort(reverse=True)
	arr2.sort()
	idx1 = 0
	idx2 = 0
	dis1 = sum1 - sum2
	dis2 = sum1 - sum2
	while (dis2>0):
		# print(5,dis2, idx2, arr2[idx2])
		dis2 = dis2 + arr2[idx2] - 9
		turns2 += 1
		idx2 += 1
	while (dis1>0):
		# print(6,dis1, idx1, arr1[idx1])
		dis1 = dis1 - arr1[idx1]
		turns1 += 1
		idx1 += 1
	print(min(turns1, turns2))
elif sum2>sum1:
	arr2.sort(reverse=True)
	arr1.sort()
	idx1 = 0
	idx2 = 0
	dis1 = sum2 - sum1
	dis2 = sum2 - sum1
	while (dis1>0):
		# print(7,dis1, idx1, arr1[idx1])
		dis1 = dis1 + arr1[idx1] - 9
		turns1 += 1
		idx1 += 1
	while (dis2>0):
		# print(8,dis2, idx2, arr2[idx2])
		dis2 = dis2 - arr2[idx2]
		turns2 += 1
		idx2 += 1
	print(min(turns1, turns2))
else:
	print(0)