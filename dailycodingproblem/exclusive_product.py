# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i. 
# Solve it without using division and in O(n).
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].

def productExcept(arr):
	res = []
	p = 1

	for i in range(len(arr)):
		res.append(p)
		p *= arr[i]

	p=1
	for i in range(len(arr)-1, -1, -1):
		res[i] *= p
		p *= arr[i]

	return res

_input1 = [1, 2, 3, 4, 5]
_output1 = [120, 60, 40, 30, 24]

assert productExcept(_input1) == _output1, 'Wrong'
