def repetitions(dna):
  i = 0
  currentSub = ''
  longest = 0
  while i<len(dna):
    currentChar = dna[i]
    if not currentSub or currentChar != currentSub[-1]:
      currentSub = currentChar # reset
    else:
      currentSub += currentChar
    longest = max(len(currentSub),longest) 
    i += 1
  return longest

def main():
  dna = [c for c in input()]
  result = repetitions(dna)
  print(result)

if __name__ == "__main__":
  main()