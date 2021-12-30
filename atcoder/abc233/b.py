l, r = map(int, input().split())
s = input()

def solve(l: int,r: int,s: str)->str:
  return s[:l-1] + s[l-1:r][::-1] + s[r:]

print(solve(l,r,s))
