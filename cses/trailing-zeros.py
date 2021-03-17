import math

def trailing_zeros(n):
  log2 = math.floor(math.log(n, 2))
  log5 = math.floor(math.log(n, 5))
  total2 = sum([n//(2**i) for i in range(1, log2+1)])
  total5 = sum([n//(5**i) for i in range(1, log5+1)])
  # print(log2, log5, total2, total5)
  return min(total2, total5)

def main():
  n = int(input())
  result = trailing_zeros(n)
  print(result)
  
if __name__ == "__main__":
  main()