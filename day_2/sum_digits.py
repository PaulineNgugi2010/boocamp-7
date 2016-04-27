def sum_digits(A):
	'''
	Takes a list A, and returns 
		the sum of all the digits 
			in the list e.g. [10, 30, 45] 
			should return 1 + 0 + 3 + 4 + 5
	'''
<<<<<<< HEAD
	total = 0
	for i  in A:
		b = str(i)
		for i in b:
			num = int(i)
			total += num
	return total
=======
 total = 0
    for i in A:
        for i in str(i):
            total += int(i)
    return total
	
	return total

>>>>>>> 0da3ec5f21071e7fed8dd023097ce5dbaae61a12

print sum_digits([10, 30, 45])	
