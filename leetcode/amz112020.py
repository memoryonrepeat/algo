# Given the set of all 4 letter words in the English language find the smallest 
# number of transformations needed to turn a 4 letter word of the set (source) 
# into another 4 letter word within the same set (target).

# A transformation is defined as a change of a single letter in the original word that produces a valid word in the given set.

transformations("POOL","SAGE") => smallest # of transformations (positive int)

def getDifference(source, target):
    result = 0
    for i,char in enumerate(source):
        if char != target[i]:
            result += 1
    return result
    
valid_words = {'TOOL': True, 'COOL': True} #....
alphabets = ['A','B','C'] #... up to Z

def recursion(source, target, count, visited):
    if source not in valid_words:
        return float("inf")
    if source == target:
        return count
    if source in visited:
        return float("inf")
    visited.add(source)
    result = float("inf")
    for i,c in enumerate(source):
        for alphabet in alphabets:
            next_source = source[:i] + alphabet + source[i+1:]
            result = min(result, recursion(next_source, target, count+1))
    return result

def transformations(source, target):
    return recursion(source, target, 0, set())
    
            
        
    