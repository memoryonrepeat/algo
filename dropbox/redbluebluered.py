# IDEA: Use hashmap with key = pattern character, value = substring of input
# Use DFS to search for the matching.

def  wordpattern(pattern, input):
	hashmap = {}
	for char in pattern:
		if char not in hashmap:
			hashmap[char]=None
	
def matching(hashmap, input):
	

print(wordpattern("abba","redbluebluered"))