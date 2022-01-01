from collections import defaultdict

n, k = map(int, input().split())

a = map(int, input().split())

prefixSums = defaultdict(int)

def solve(n,k,a):
  s = 0
  result = 0

  for num in a:
    s += num
    if s - k in prefixSums:
      result += prefixSums[s-k]
    if s == k:
      result += 1
    prefixSums[s] += 1

  return result

print(solve(n,k,a))