def missing_number(n, existing):
  return set(range(1,n+1)) - set(existing)

def main():
  n = int(input())
  existing = [int(i) for i in input().split()]
  result = missing_number(n, existing)
  print(' '.join(str(i) for i in result))

if __name__ == "__main__":
  main()