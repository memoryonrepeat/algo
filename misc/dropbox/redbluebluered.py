# IDEA: Use hashmap with key = pattern character, value = substring of input
# Use DFS to search for the matching.
	
import copy

def check(pattern, input):
	if len(input)<len(pattern):
		return False
	letters = []
	for char in pattern:
		if not char in letters:
			letters.append(char)
	if backtrack({}, pattern, input, 0, letters):
		return True
	return False

# letters = letters yet to be matched
def backtrack(hashmap, pattern, input, start, letters):
	# base case
	print(hashmap, start, letters)
	if not letters:
		mapping_result = ""
		for char in pattern:
			mapping_result += hashmap[char]
		if mapping_result == input:
			print(hashmap, start, letters, True)
			return True
		return False
	else:
		if start == len(input):
			return False
		else:
			# backtrack
			for char in letters:
				new_letters = [c for c in letters if c!=char]
				for i in range(start+1,len(input)+1):
					new_hashmap = copy.deepcopy(hashmap)
					new_hashmap[char]=input[start:i]
					if backtrack(new_hashmap, pattern, input, i, new_letters):
						return True
	return False

pattern = 'abac'

input = 'rrkkrrt'
# input = 'xml'

print(check(pattern, input))