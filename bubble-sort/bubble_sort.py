from sys import argv, stdin

in_file = 'in.txt'
out_file = 'out.txt'

in_stream = open(in_file,'r')
out_stream = open(out_file,'w')


def bubble_sort(list_of_num):

	swapped = True
	offset = 0
	while swapped:
		swapped = False
		offset += 1
		for i in range(len(list_of_num)-offset):
			if list_of_num[i]>list_of_num[i+1]:
				list_of_num[i],list_of_num[i+1] = list_of_num[i+1],list_of_num[i]
				swapped = True
	return list_of_num

def main():

	from random import shuffle

   	testset = range(100)
   	testcase = testset[:]
   	shuffle(testcase)
   	assert (testcase != testset),'Test set not shuffled' 
   	bubble_sort(testcase)
   	assert (testcase == testset), 'Sorting was wrong'
    
	# input = [int(x) for x in in_stream.readline().split()]
	# print bubble_sort(input)

if __name__ == '__main__':
	main()