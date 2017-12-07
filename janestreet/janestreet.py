# Complete the function below.

from collections import Counter

# Check if a string is a programmer string
def is_programmer_string(s):
    s = Counter(s)
    programmer = Counter('programmer')
    return all(programmer[letter] <= s[letter] for letter in programmer)

# Use 2 pointers coming from left and right of the minimal possible case: programmerprogrammer
# Then move the left pointer to the right and right pointer to the left
# If at some point both substrings on left and right are programmer string then every indices
# between left and right pointers are valid
# Else if left pointer has gone past right pointer and still nothing found then there is no such indice.
def  programmerStrings(s):
    if len(s) < 2*len('programmer')+1:
        return 0
    start = len('programmer')
    end = len(s)-1-len('programmer')
    while (start<=end):
        has_string_left = is_programmer_string(s[0:start])
        has_string_right = is_programmer_string(s[end+1:len(s)])
        condition = has_string_left and has_string_right
        # print(start,end,condition,has_string_left,has_string_right,s[end+1:len(s)])
        if condition:
            return end-start+1
        if not has_string_left:
            start += 1
        if not has_string_right:
            end -= 1
    return 0
    
