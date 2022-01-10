s = [c for c in input()]

s.sort()

combinations = []

def solve(current, remaining):
  if not remaining:
    combinations.append(current)
    return
  
  # Intuition:
  # To generate the combinations, we generate a DFS tree and collect the leaves
  # However there are lots of duplications due to the same char potentially being chosen repeatedly at each level
  # Therefore, before going deeper, we make sure that the options at each level are unique
  for c in set(remaining):
    i = remaining.index(c)
    solve(current + c, remaining[:i] + remaining[i+1:])

solve('', s)

combinations = combinations

print(len(combinations))

for c in combinations:
  print(c)