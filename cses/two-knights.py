def two_knights(n):
  if n<2:
    return 0
  if n==2:
    return 6
  total = n*n * (n*n-1) // 2
  collisions =  4 * (n-1) * (n-2)
  return total - collisions

def main():
  n = int(input())
  results = []
  for i in range(1,n+1):
    results.append(two_knights(i))
  for r in results:
    print(r)

if __name__ == "__main__":
  main()