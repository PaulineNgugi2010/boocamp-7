def super_sum(*args):
	'''
	Takes in variable number of items,
	and returns the sum.
	e.g super_sum(10, 20) =30
		super_sum(10, 20, 40) =70
		super_sum(1, 4, 5, 6, 7) =23
	'''
#like need for overloading parameters
	total =0
	for i in args:
		total += i
	return total
a = [10, 20]
b = [10, 20, 40]
c = [1, 4, 5, 7]


print super_sum(*a)
print super_sum(*b)
print super_sum(*c)

