def permutations1(head, tail=''):
    if len(head) == 0: print 'result->',tail
    else:
        for i in range(len(head)):
            print head[0:i],head[i+1:],tail+head[i] # tracing recursion tree
            permutations1(head[0:i] + head[i+1:], tail+head[i])

def permutations2(s):
   if len(s) == 1:
     return [s]

   result = [] # resulting list
   for char in s:
     remaining_elements = [x for x in s if x != char]
     remaining_permutations = permutations2(remaining_elements) # permutations of sublist

     for permutation in remaining_permutations:
       result.append([char] + permutation)

   return result

permutations1('abcd')
print permutations2('abcd')