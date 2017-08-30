# IDEA: Use hashmap with key = pattern character, value = substring of input
# Use DFS to search for the matching.
	
def check(pattern, input):
	if len(input)<len(pattern):
		return False
	if backtrack({}, pattern, input, ""):
		return True
	return False

def backtrack(hashmap, pattern, input, mapresult):
	# base
	if len(input)<len(pattern):
		return False
	elif len(input)==len(pattern):
		if len(input)==0:
			return True
		return False

	# backtrack
	for i,char in enumerate(pattern):
		if char in hashmap:
			if backtrack(hashmap, pattern[i:], input[len(hashmap[char]):], mapresult+hashmap[char]):
				return True
		else:
			for j in range(len(input)):
				hashmap[char] = input[:j]
				if backtrack(hashmap, pattern[i:], input[j:], mapresult+hashmap[char]):
					return True
	return False

def isMatch(hashmap, pattern, input):
	test = pattern
	for key in hashmap:
		test = test.replace(key, hashmap[key])
	return test==input

pattern = 'abba'

input = 'redbluebluered'

print(check(pattern, input))