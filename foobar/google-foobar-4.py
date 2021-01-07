# find lucky triples
def solution(l):
	count = 0
	for i in range(1,len(l)-1):
		current = l[i]
		count += len([j for j in l[:i] if current%j==0]) * len([k for k in l[i+1:] if k%current==0])
	return count
    
l = [1,1,1]
print(solution(l))