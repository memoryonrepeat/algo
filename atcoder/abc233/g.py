from functools import lru_cache

n = int(input())
matrix = []
for i in range(n):
  matrix.append([c for c in input()])

@lru_cache(maxsize = None)
def solve(minX, minY, maxX, maxY):
  if maxX < minX or maxY < minY:
    return 0

  result = max(maxX - minX + 1, maxY - minY + 1)

  # Scan empty rows
  for r in range(minY, maxY+1):
    isEmpty = True
    for c in range(minX, maxX+1):
      if matrix[r][c] == '#':
        isEmpty = False
        break
    if isEmpty:
      result = min(result, solve(minX, r+1, maxX, maxY) + solve(minX, minY, maxX, r-1))

  # Scan empty columns
  for c in range(minX, maxX+1):
    isEmpty = True
    for r in range(minY, maxY+1):
      if matrix[r][c] == '#':
        isEmpty = False
        break
    if isEmpty:
      result = min(result, solve(c+1, minY, maxX, maxY) + solve(minX, minY, c-1, maxY))

  return result

print(solve(0,0,n-1,n-1))