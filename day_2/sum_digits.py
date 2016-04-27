def sum_digits(A):
	'''
	Takes a list A, and returns 
		the sum of all the digits 
			in the list e.g. [10, 30, 45] 
			should return 1 + 0 + 3 + 4 + 5
	'''
	total = 0
	for i  in A:
		b = str(i)
		for i in b:
			num = int(i)
			total += num
	return total

print sum_digits([10, 30, 45])	
