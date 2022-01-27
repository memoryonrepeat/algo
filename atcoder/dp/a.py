from functools import lru_cache

# Not limiting recursion stack results in runtime error in some testcases
# Happens on Atcoder judge only
import sys
sys.setrecursionlimit(1000000)

n = int(input())

h = list(map(int, input().split(' ')))

@lru_cache(maxsize = None)
def solve(stone):
  if stone == n:
    return 0
  if stone == n-1:
    return solve(stone+1) + abs(h[stone-1] - h[stone])
  return min(solve(stone+1) + abs(h[stone-1] - h[stone]), solve(stone+2) + abs(h[stone-1] - h[stone+1]))

print(solve(1))