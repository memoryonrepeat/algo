# def _generate_strings(seed):
#   seed.sort()
#   answer = []

#   def backtrack(s):
#     if len(s) <= 1:
#       return s
#     for i,c in enumerate(s):
#       localResult = s[:i] + 
      
#   backtrack(seed)

#   return ans

def generate_strings(s):
  if len(s) == 1:
    return s

  result = []  # resulting list
  for i in range(len(s)):
    remaining_permutations = generate_strings(s[i+1:])  # permutations of sublist

    for permutation in remaining_permutations:
      # print(s[:i],permutation)
      result.append(s[:i+1] + permutation)

  return result

def main():
  seed = input()
  seed = ''.join(sorted(s))
  allStrings = generate_strings(seed)
  print(len(allStrings))
  for string in allStrings:
    print(string)
  
if __name__ == "__main__":
  main()