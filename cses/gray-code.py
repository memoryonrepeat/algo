def gray_code(n):
  results = [0]
  for i in range(n):
      results += [x + pow(2, i) for x in reversed(results)]
  return results

def main():
  n = int(input())
  result = gray_code(n)
  # print(result)
  print('\n'.join(map(lambda x: f'{x:0{n}b}',result)))
  
if __name__ == "__main__":
  main()