def data_type(x):
	'''
	Takes an argument, x:
		-For a integer, return x**2
		-For a float, return x/2
		-For a string, return "Hello "+ x
		-For a boolean, return "boolean"
		-For a long, return  squareroot(x)
	'''
	if type(x) == int:
		return x **2
	elif type(x) ==float:
		return x / 2
	elif type(x) == str:
		return "Hello {}".format(x)
	elif type(x) ==long:
		return "long"
	elif type(x) == bool:
		return "boolean"
	else:
	 return "No category found"

print data_type(5)
print data_type(4.5)
print data_type(500000L)
print data_type(5>2)
print data_type("Pauline")