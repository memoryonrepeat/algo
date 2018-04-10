def solution(string_list, n):
    string_counter = {}
    result = set()
    for string in string_list:
        if string in string_counter:
            string_counter[string] += 1
        else:
            string_counter[string] = 1
        if string_counter[string] == n:
            result.add(string)
        elif string_counter[string]>n:
            result.discard(string)
    return result

def test():
	# Tests
	assert solution(['s1','s2','s3','s1','s1','s2'],1)=={'s3'}, solution(['s1','s2','s3','s1','s1','s2'],1)
	assert solution(['s1','s2','s3','s1','s1','s2'],2)=={'s2'}, solution(['s1','s2','s3','s1','s1','s2'],2)
	assert solution(['s1','s2','s3','s1','s1','s2'],3)=={'s1'}, solution(['s1','s2','s3','s1','s1','s2'],3)
	assert solution(['s1','s2','s3','s1','s1','s2'],4)==set(), solution(['s1','s2','s3','s1','s1','s2'],4)
	assert solution([],1)==set(), solution([],1)
	assert solution(['s1','s2','s3','s1','s1','s2','s2'],3)=={'s1','s2'}, solution(['s1','s2','s3','s1','s1','s2','s2'],3)

test()
