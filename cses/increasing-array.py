def increasing_array(n, existing):
  result = 0
  i = 1
  prev = existing[0]
  while i<len(existing):
    # print(i,existing[i], prev, result)
    if existing[i]<prev:
      result += prev - existing[i]
    prev = max(existing[i],prev)
    i += 1
  return result

def main():
  n = int(input())
  existing = [int(i) for i in input().split()]
  result = increasing_array(n, existing)
  print(result)

if __name__ == "__main__":
  main()