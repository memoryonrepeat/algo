n, x = map(int, input().split())

matrix = []

for i in range(n):
  matrix.append(list(map(int, input().split()))[1:])

def solve(currentRow, currentProduct, target):
  if currentRow > n-1:
    if currentProduct == target:
      return 1
    else:
      return 0
  neighbors = [i for i in matrix[currentRow] if target%i == 0]
  result = 0
  while neighbors:
    current = neighbors.pop()
    result += solve(currentRow+1, currentProduct*current, target)
  return result

print(solve(0,1,x))
