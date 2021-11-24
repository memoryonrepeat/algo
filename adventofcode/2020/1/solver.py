with open('input.txt') as f:
  input = [int(line.rstrip('\n')) for line in f.readlines()] 

# print(input)

# Solve two sum using two pointers
def solve0(input):
  input.sort()
  start = 0
  end = len(input) - 1
  
  while input[start] + input[end] != 2020:
    if input[start] + input[end] < 2020:
      start += 1
    else:
      end -= 1
    if start >= end:
      break
  
  if input[start] + input[end] != 2020:
    return None
  return input[start] * input[end]

print(solve0(input))

from collections import Counter

# Solve two sum using counter
def solve1(input):
  c = Counter(input)
  for num in input:
    if 2020-num in c and num != 2020-num:
      return num * (2020-num)
  return None

print(solve1(input))

# Solve three sum using counter
def solve2(input):
  c = Counter(input)
  for num1 in c:
    c[num1] -= 1
    for num2 in c:
      if c[num2] > 0:
        c[num2] -= 1
      else:
        continue
      if 2020-num1-num2 in c and c[2020-num1-num2]>0:
        return num1*num2*(2020-num1-num2)
      else:
        c[num2] += 1
    c[num1] += 1
  return None

print(solve2(input))
        
  
