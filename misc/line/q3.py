# Bottom up dynamic programming
# f(n) = sum(f(n-k)) for k=1..6
def calculate(n):
	dp_table = {
		0: 1,
		1: 1
	}
	for i in range(2,n+1):
		dp_table[i] = 0
		for j in range(1,7):
			if i-j>=0:
				dp_table[i] += dp_table[i-j]
	return dp_table[n]

# 14527490260516100855695859704819627818108010882741117227956927412305738742399171256642436462028811566617818991926058940988565927870172608545709804976244851391054850231415387973537361

print(calculate(610))