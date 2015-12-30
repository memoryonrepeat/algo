from sys import argv, stdin

if len(argv) < 2:
    input = stdin
else:
    input = open(argv[1])

M,N = [int(x) for x in input.readline().split()]

matrix = [[0 for x in range(N)] for x in range(M)] 
dp_table = [[-1 for x in range(N)] for x in range(M)] 

for row in range(M):                
    matrix[row] = [int(x) for x in input.readline().split()]

number_of_employee = int(input.readline())

#Use a dictionary {employee : [i,j]} 
starting_point = {}

for i in range(number_of_employee):
    starting_point[i] = [int(x) for x in input.readline().split()]

#Use a memoization table for dynamic programming    
def fastest_time(i,j):    
    
    #If optimal value already calculated then just return
    if (dp_table[i][j]>-1):
        return dp_table[i][j]
    
    #Base case: at the office
    if (i==M-1) and (j==N-1):        
        dp_table[i][j] = matrix[i][j]
        return matrix[i][j]
    
    #Base case: at the last row
    elif (i==M-1) and (j<N-1):        
        dp_table[i][j] = matrix[i][j] + fastest_time(i,j+1)
        return dp_table[i][j]
    
    #Base case: at the last column
    elif (i<M-1) and (j==N-1):
        dp_table[i][j] = matrix[i][j] + fastest_time(i+1,j)
        return dp_table[i][j]
    
    #The rest
    else:
        dp_table[i][j] = matrix[i][j] + min(fastest_time(i,j+1),fastest_time(i+1,j))
        return dp_table[i][j]

for i in range(number_of_employee):
    print fastest_time(starting_point[i][0],starting_point[i][1])
