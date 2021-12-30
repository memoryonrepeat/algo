x, y = map(int, input().split())

def solve(x: int,y: int)->int:
  return max(0, (y-x)//10 + min(1,(y-x)%10))

print(solve(x,y))