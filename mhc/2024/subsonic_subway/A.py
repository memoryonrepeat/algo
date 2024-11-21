# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/A

f = open("subsonic_subway_input.txt", "r")

T = int(f.readline())
result = []

# Translate windows to pairs of min / max velocity required for each stop
# Then merge those intervals, output -1 if impossible to converge to 1 interval
def solve(windows):
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
		current[1] = max(current[1], high)

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

print("\n".join(["Case #{i}: {r:.10f}".format(i=i+1,r=result[i]) for i in range(len(result))]))