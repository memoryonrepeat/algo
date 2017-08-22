# We'll say that a "triple" in a string is when a char appears three times in a row. Return the number of triples in the given string. The triples may overlap. 

# countTriple("abcXXXabc") → 1
# countTriple("xxxabyyyycd") → 3
# countTriple("a") → 0


def solution(str):
    count = 0
    curr = 0
    while (curr<len(str)-2):
        if str[curr]==str[curr+1] and str[curr]==str[curr+2]:
            count += 1
            curr += 1
        else:
            curr += 1
    return count

print(solution("xxxabyyyycd"))