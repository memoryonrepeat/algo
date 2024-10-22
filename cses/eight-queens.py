from collections import defaultdict

total = 0
occupied = defaultdict(list)

for row in range(8):
	line = list(input())
	for col in range(8):
		if line[col] == "*":
			occupied[row].append(col)

def getCandidates(row, currentBoard):
	pool = [i for i in range(8) if i not in occupied[row]]
	candidates = []
	for col in pool:
		conflict = False
		for i,j in currentBoard:
			if (col == j) or (row-col == i-j) or (row+col == i+j):
				conflict = True
				break
		if not conflict:
			candidates.append(col)

	return candidates


def solve(currentRow, currentBoard):
	global total
	# Column candidates for current row
	candidates = getCandidates(currentRow, currentBoard)
	if currentRow == 7:
		total += len(candidates)
	for candidate in candidates:
		solve(currentRow+1, currentBoard + [[currentRow,candidate]])

solve(0, [])

print(total)