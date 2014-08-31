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



