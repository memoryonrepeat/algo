def coin_piles(m,n):
  if (2*m - n) >= 0 and (2*m - n) % 3 == 0 and (2*n - m) >= 0 and (2*n - m) % 3 == 0:
    return 'YES'
  return 'NO'

def main():
  n = int(input())
  results = []
  for i in range(n):
    m,n = [int(i) for i in input().split()]
    results.append(coin_piles(m,n))
  for r in results:
    print(r)

if __name__ == "__main__":
  main()