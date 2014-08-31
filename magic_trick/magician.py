# Recently you went to a magic show. You were very impressed by one of the tricks, so you decided to try to figure out the secret behind it!

# The magician starts by arranging 16 cards in a square grid: 4 rows of cards, with 4 cards in each row. Each card has a different number from 1 to 16 written on the side that is showing. Next, the magician asks a volunteer to choose a card, and to tell him which row that card is in.

# Finally, the magician arranges the 16 cards in a square grid again, possibly in a different order. Once again, he asks the volunteer which row her card is in. With only the answers to these two questions, the magician then correctly determines which card the volunteer chose. Amazing, right?

# You decide to write a program to help you understand the magician's technique. The program will be given the two arrangements of the cards, and the volunteer's answers to the two questions: the row number of the selected card in the first arrangement, and the row number of the selected card in the second arrangement. The rows are numbered 1 to 4 from top to bottom.

# Your program should determine which card the volunteer chose; or if there is more than one card the volunteer might have chosen (the magician did a bad job); or if there's no card consistent with the volunteer's answers (the volunteer cheated).

# Input

# The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing an integer: the answer to the first question. The next 4 lines represent the first arrangement of the cards: each contains 4 integers, separated by a single space. The next line contains the answer to the second question, and the following four lines contain the second arrangement in the same format.

# Output

# For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1).

# If there is a single card the volunteer could have chosen, y should be the number on the card. If there are multiple cards the volunteer could have chosen, y should be "Bad magician!", without the quotes. If there are no cards consistent with the volunteer's answers, y should be "Volunteer cheated!", without the quotes. The text needs to be exactly right, so consider copying/pasting it from here.

# Limits

# 1 ≤ T ≤ 100.
# 1 ≤ both answers ≤ 4.
# Each number from 1 to 16 will appear exactly once in each arrangement.

from __future__ import division

IN_FILE_NAME = 'test.in'
OUT_FILE_NAME = 'test.out'
GRID_SIZE = 4

grid_1 = [[0]*GRID_SIZE for x in xrange(GRID_SIZE)]
grid_2 = [[0]*GRID_SIZE for x in xrange(GRID_SIZE)]

def solve(grid_1,grid_2,first_ans,second_ans):
	result=''
	count=0	
	
	for key1 in grid_1[first_ans]:		
		for key2 in grid_2[second_ans]:			
			if key1==key2:
				result=key1				
				count += 1
	if count>1:
		result='Bad magician!'
	elif count==0:
		result='Volunteer cheated!'	
	return result

	

def main():
	in_file = open(IN_FILE_NAME,'r')
	out_file = open(OUT_FILE_NAME,'w')
	number_of_cases = in_file.readline()
	for case in range(1,int(number_of_cases)+1):

		first_ans = int(in_file.readline())-1
		for i in range(0,GRID_SIZE):
			row_values=in_file.readline().split(' ')			
			for idx,val in enumerate(row_values):				
				grid_1[i][idx] = int(val)

		second_ans = int(in_file.readline())-1
		for i in range(0,GRID_SIZE):
			row_values=in_file.readline().split(' ')
			for idx,val in enumerate(row_values):
				grid_2[i][idx] = int(val)
		
		result = solve(grid_1,grid_2,first_ans,second_ans)

		to_write = 'Case #'+str(case)+': '+str(result)+'\n'
		out_file.write(to_write)
main()



