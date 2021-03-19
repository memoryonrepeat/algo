from collections import Counter

def palindrome_reorder(s):
  if len(s)%2 == 0:
    allowedOddCounts = 0
  else:
    allowedOddCounts = 1
  counter = Counter(s)
  oddCounts = 0
  s = ''
  for key in counter:
    if counter[key] % 2 != 0:
      oddCounts += 1
      s += key
      if oddCounts > allowedOddCounts:
        return 'NO SOLUTION'
  if s:
    counter[s] -= 1
  for key in counter:
    s = key * (counter[key]//2) + s + key * (counter[key]//2)
    counter[key] = 0
  return s

def main():
  s = input()
  result = palindrome_reorder(s)
  print(result)
  
if __name__ == "__main__":
  main()