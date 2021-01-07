# salute count
def solution(s):
    i = 0
    left_count = 0
    count = 0
    while i<len(s):
    	if s[i] == '>':
    		left_count += 1
    	elif s[i] == '<':
    		count += left_count

    	i += 1

    return count*2

s = '-----><'

print(solution(s))