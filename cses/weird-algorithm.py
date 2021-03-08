def simulate(n):
  result = [n]
  while n>1:
    if n%2 == 1:
      n = n*3+1
    else:
      n = n//2
    result.append(n)
  return result

def main():
  n = int(input())
  result = simulate(n)
  print(' '.join(str(i) for i in result))

if __name__ == "__main__":
  main()