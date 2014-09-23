#assume that array is sorted ascendingly, i.e a[0]<a[1]<a[2]...
def binary_search(arr,x):

	#Out of bound
	if (x<arr[0]) or (x>arr[-1]):
		return False
	
	mid = len(arr)/2
	if (x==arr[mid]):
		return True

	first_half = arr[:mid]
	second_half = arr[mid:]			

	if (x>arr[mid]):
		return binary_search(second_half,x)
	else:			
		return binary_search(first_half,x)

if __name__ == '__main__':	

	#Use assertion for testing
	assert(binary_search([1,2,4,6,7,9],6)==True),'Binary search was wrong'
	assert(binary_search([1,2,4,6,7,9],8)==False),'Binary search was wrong'

	print binary_search([1,2,4,6,7,9],6)
	print binary_search([1,2,4,6,7,9],8)