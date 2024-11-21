# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/A

f = open("subsonic_subway_input.txt", "r")

T = int(f.readline())
result = []

# Translate windows to pairs of min / max velocity required for each stop
# Then merge those intervals, output -1 if impossible to converge to 1 interval
def solve(windows):
	minVelocity = 1/windows[0][1]
	maxVelocity = 1/windows[0][0] if windows[0][0] > 0 else 999999999999
	for i in range(1,len(windows)):
		minVelocity = max(minVelocity, (i+1)/windows[i][1])
		if windows[i][0] == 0:
			maxVelocity = min(maxVelocity, 999999999999)
		else:
			maxVelocity = min(maxVelocity, (i+1)/windows[i][0])
	# print(windows, minVelocity, maxVelocity)

	if minVelocity > maxVelocity:
		result.append(-1)
		return
	result.append(minVelocity)


for _ in range(T):
	n = int(f.readline())
	windows = []
	for _ in range(n):
		a,b = map(int, f.readline().split(" "))
		windows.append([a,b])
	solve(windows)


f.close()
fw = open("result.txt", "w")
to_write = "\n".join(["Case #{i}: {r:.7f}".format(i=i+1,r=result[i]) for i in range(len(result))])
fw.write(to_write)
fw.close()