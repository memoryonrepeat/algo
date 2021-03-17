def bit_strings(n):
  return 2**n % (10**9 + 7)

def main():
  n = int(input())
  result = bit_strings(n)
  print(result)
  
if __name__ == "__main__":
  main()