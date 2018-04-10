# Solution in Python 3 - there is no limit for integers
# Use bottom-up dynamic programming to avoid call stack overflow
def f(n):
	
	dp_table = {
		0: 0,
		1: 1
	}

	for i in range(2,n+1):
		dp_table[i] = dp_table[i-1] + dp_table[i-2]
	return dp_table[n]

print(f(8181))