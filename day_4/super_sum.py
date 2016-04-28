def super_sum(*args):

	'''
	Returns a sum of numbers 
	e.g
		super_sum(1,2,3) ==> 6
		super_sum([1,2,3]) ==> 6

		super_sum([10],[2],[3]) ==> 60'''
	

	total = 0
	if not args:
		return 0

	else:
		for x in args:
			if type(x) == list:
				#x= is now ([1, 2, 3])
				for y in x:
					total += y
			
			elif type(x) == str:
				return 0
			
			else:
				total +=  x
		
		return total
	
'''for x in args:
			b = str(x)
			for y in b:
				num = int(y)
				total += num
		return total'''






