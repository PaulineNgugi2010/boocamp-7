def hello(name,age, class_=''):
	'''
	Explains how to pass arguments
	'''
	if class_ == False:
		return "I am {}, {} and class {}".format(name, age, class_)
	return "I am {}, my age is {}".format(name, age)

 
people = [
			("Jane", 23, 0),
			("Joe", 23, 9),
			("Brian", 23),
			("Betty", 23),

			]
for i in people:
	print hello(*i)

