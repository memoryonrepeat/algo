def spiral(y,x):
  if y>x:
    diagonal = y*y - y + 1
    if y%2 == 0: # increasing from diagonal
      return diagonal + (y-x)
    else: # decreasing from diagonal
      return diagonal - (y-x)
  else:
    diagonal = x*x - x + 1
    # print(y,x,diagonal)
    if x%2 == 0: # decreasing from diagonal
      # print(y,x, 'decreasing')
      return diagonal - (x-y)
    else: # increasing from diagonal
      # print(y,x, 'increasing')
      return diagonal + (x-y)

def main():
  n = int(input())
  results = []
  for i in range(n):
    y,x = [int(i) for i in input().split()]
    results.append(spiral(y,x))
  for r in results:
    print(r)

if __name__ == "__main__":
  main()