from functools import reduce
from collections import Counter
N = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
mean = reduce((lambda x,y: x+y), arr)/N
median = arr[(N+1)//2] if N%2==1 else (arr[N//2]+arr[N//2-1])/2
c = reduce((lambda x,y: x if x[1]>y[1] else (y if x[1]<y[1] else (x if x<y else y))),Counter(arr).items()) 
print(mean)
print(median)
print(c[0])