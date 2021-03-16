def two_sets(n):
  total_sum = n * (n+1) // 2

  if total_sum % 2 != 0:
    return ()

  part_sum = n * (n+1) // 4
  set1 = set()
  takeHead = True
  currentHead = 1
  currentTail = n

  while True:
    # print(part_sum, takeHead, currentHead, currentTail, set1)
    if takeHead:
      if part_sum > currentHead:
        set1.add(currentHead)
        part_sum -= currentHead
        currentHead += 1
        takeHead = False
      else:
        set1.add(part_sum)
        break
    else:
      if part_sum > currentTail:
        set1.add(currentTail)
        part_sum -= currentTail
        currentTail -= 1
        takeHead = True
      else:
        set1.add(part_sum)
        break

  return (list(set1), list(set(range(1,n+1)) - set1))
  

def main():
  n = int(input())
  result = two_sets(n)
  if len(result) < 2:
    print('NO')
    return
  print('YES')
  print(len(result[0]))
  print(' '.join(map(str, result[0])))
  print(len(result[1]))
  print(' '.join(map(str, result[1])))
  
if __name__ == "__main__":
  main()