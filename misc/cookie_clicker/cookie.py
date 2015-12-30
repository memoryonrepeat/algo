# Problem

# In this problem, you start with 0 cookies. You gain cookies at a rate of 2 cookies per second, by clicking on a giant cookie. Any time you have at least C cookies, you can buy a cookie farm. Every time you buy a cookie farm, it costs you C cookies and gives you an extra F cookies per second.

# Once you have X cookies that you haven't spent on farms, you win! Figure out how long it will take you to win if you use the best possible strategy.

# Example

# Suppose C=500.0, F=4.0 and X=2000.0. Here's how the best possible strategy plays out:

# You start with 0 cookies, but producing 2 cookies per second.
# After 250 seconds, you will have C=500 cookies and can buy a farm that produces F=4 cookies per second.
# After buying the farm, you have 0 cookies, and your total cookie production is 6 cookies per second.
# The next farm will cost 500 cookies, which you can buy after about 83.3333333 seconds.
# After buying your second farm, you have 0 cookies, and your total cookie production is 10 cookies per second.
# Another farm will cost 500 cookies, which you can buy after 50 seconds.
# After buying your third farm, you have 0 cookies, and your total cookie production is 14 cookies per second.
# Another farm would cost 500 cookies, but it actually makes sense not to buy it: instead you can just wait until you have X=2000 cookies, which takes about 142.8571429 seconds.
# Total time: 250 + 83.3333333 + 50 + 142.8571429 = 526.1904762 seconds.
# Notice that you get cookies continuously: so 0.1 seconds after the game starts you'll have 0.2 cookies, and π seconds after the game starts you'll have 2π cookies.

# Input

# The first line of the input gives the number of test cases, T. T lines follow. Each line contains three space-separated real-valued numbers: C, F and X, whose meanings are described earlier in the problem statement.

# C, F and X will each consist of at least 1 digit followed by 1 decimal point followed by from 1 to 5 digits. There will be no leading zeroes.

# Output

# For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of seconds it takes before you can have X delicious cookies.

# We recommend outputting y to 7 decimal places, but it is not required. y will be considered correct if it is close enough to the correct number: within an absolute or relative error of 10-6. See the FAQ for an explanation of what that means, and what formats of real numbers we accept.

# Limits

# 1 ≤ T ≤ 100.

# Small dataset

# 1 ≤ C ≤ 500.
# 1 ≤ F ≤ 4.
# 1 ≤ X ≤ 2000.
# Large dataset

# 1 ≤ C ≤ 10000.
# 1 ≤ F ≤ 100.
# 1 ≤ X ≤ 100000.


from __future__ import division

R=2
IN_FILE_NAME = 'test.in'
OUT_FILE_NAME = 'test.out'

def solve(X,F,C,R):
	total_time = 0
	time_left_not_buying = X/R
	time_left_buying = C/R + X/(R+F)

	while time_left_buying < time_left_not_buying:
		total_time += C/R
		R += F	
		time_left_not_buying = X/R
		time_left_buying = C/R + X/(R+F)

	total_time += X/R
	return total_time

def main():
	in_file = open(IN_FILE_NAME,'r')
	out_file = open(OUT_FILE_NAME,'w')
	number_of_cases = in_file.readline()
	for case in range(1,int(number_of_cases)+1):
		data = in_file.readline().split(' ')

		C=float(data[0])
		F=float(data[1])
		X=float(data[2])
		
		result = solve(X,F,C,R)
		to_write = 'Case #'+str(case)+': '+str(result)+'\n'
		out_file.write(to_write)
main()



