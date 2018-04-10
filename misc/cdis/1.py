def flatten_list(nested_list):
	flattened = []
	for val in nested_list:
		if not isinstance(val, list):
			flattened += [val]
		else:
			flattened += flatten_list(val)
	return flattened
    
assert flatten_list([2,[[3,[4]], 5]])==[2,3,4,5], flatten_list([2,[[3,[4]], 5]])