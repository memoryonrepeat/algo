def compress(s):
	curr = s[0]
	next_i = 0
	count = 0
	compressed = ""
	while next_i<len(s):
		if s[next_i]==curr:
			count += 1
		else:
			compressed += curr
			curr = s[next_i]
			if count>1:
				compressed += str(count)
			count=1
		next_i += 1
		if next_i==len(s): # last char, just write everything
			compressed += curr if count==1 else curr + str(count)

	return compressed

print(compress("aaabbbbbcccddeeeee"))