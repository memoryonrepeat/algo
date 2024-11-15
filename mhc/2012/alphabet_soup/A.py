# https://www.facebook.com/codingcompetitions/hacker-cup/2012/qualification-round/problems/A

from collections import Counter

f = open("alphabet_soup_input.txt", "r")

N = int(f.readline())

sentences = [f.readline() for _ in range(N)]

counters = [Counter(sentence) for sentence in sentences]

target = Counter("HACKERCUP")

result = []

for counter in counters:
	current = 0
	notEnough = False
	while True:
		for k,v in target.items():
			if k not in counter:
				notEnough = True
				break
			counter[k] -= v
			if counter[k] < 0:
				notEnough = True
				break
		if notEnough:
			break
		current += 1

	result.append(current)

print("\n".join(["Case #{i}: {r}".format(i=i+1,r=result[i]) for i in range(len(result))]))