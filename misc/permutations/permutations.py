def permutations1(head, tail=''):
  if len(head) == 0:
    print('result->', tail)
  else:
    for i in range(len(head)):
      print(head[0:i], head[i + 1:], tail + head[i])  # tracing recursion tree
      permutations1(head[0:i] + head[i + 1:], tail + head[i])


def permutations2(s):
  if len(s) == 1:
    return [s]

  result = []  # resulting list
  for char in s:
    remaining_elements = [x for x in s if x != char]
    remaining_permutations = permutations2(remaining_elements)  # permutations of sublist

    for permutation in remaining_permutations:
      result.append([char] + permutation)

  return result

# Using backtracking to push/pop elements before/after recursive calls
def permutations3(l):
  def dfs(candidates, currentPath, result):
    if len(currentPath) == len(l):
      result.append(currentPath[:])
      return
    
    for i, c in enumerate(candidates):
      currentPath.append(c)
      dfs(candidates[:i]+candidates[i+1:], currentPath, result)
      currentPath.pop()

    return result
  return dfs(l, [], [])

#permutations1('abcd')
print(permutations2('abcd'), len(permutations2('abcd')))
print(permutations3(['a','b','c','d']), len(permutations3(['a','b','c','d'])))
