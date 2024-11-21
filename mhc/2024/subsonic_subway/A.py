# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/A

f = open("subsonic_subway_input.txt", "r")

T = int(f.readline())
result = []

# Translate windows to pairs of min / max velocity required for each stop
# Solve by comparing min / max required velocity only
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

# Solve by merging intervals
def __solve(windows):
	intervals = []
	for i in range(len(windows)):
		if windows[i][0] == 0:
			windows[i][0] = 0.000000001
		intervals.append([(i+1)/windows[i][1], (i+1)/windows[i][0]])

	intervals.sort(key = lambda v: v[0])

	current = None
	impossible = False

	for low,high in intervals:
		if not current:
			current = [low,high]
			continue
		if low > current[1]:
			impossible = True
			break
		current[0] = max(current[0], low)
		current[1] = min(current[1], high)

	if impossible:
		result.append(-1)
		return
	result.append(current[0])

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