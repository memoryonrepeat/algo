n = int(input())
 
apples = list(map(int, input().split(' ')))

totalSum = sum(apples)

def solve(index, sum1, sum2):
  global apples
  global totalSum

  if index == len(apples):
    return abs(sum1 - sum2)

  return min(solve(index+1, sum1 + apples[index], sum2), solve(index+1, sum1, sum2 + apples[index]))

print(solve(0, 0, 0))