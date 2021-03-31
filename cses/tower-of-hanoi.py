def tower_of_hanoi(n, fr, mid, to):
  if n == 1:
    print(f'{fr} {to}')
    return
  tower_of_hanoi(n-1, fr, to, mid)
  print(f'{fr} {to}')
  tower_of_hanoi(n-1, mid, fr, to)

def main():
  n = int(input())
  print(2**n-1)
  tower_of_hanoi(n, 1, 2, 3)
  
if __name__ == "__main__":
  main()