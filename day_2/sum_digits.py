def sum_digits(A):
	'''
	Takes a list A, and returns 
		the sum of all the digits 
			in the list e.g. [10, 30, 45] 
			should return 1 + 0 + 3 + 4 + 5
	'''
	counter = 0
	
	for i in A:
		p = str(i)
		for j in p:
			counter += int(j)
	
	return counter


print sum_digits([10, 30, 45])	
