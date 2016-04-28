def add(a, b):

  	if type(a) ==int and type(b) ==int:
		print a + b
	elif type(a) ==float and type(b) ==float:
		print a + b
	elif type(a) ==list and type(b) ==list:
		print a + b
	elif type(a) ==str or type(b) ==str:
		print str(a) + str(b)
	else:
		print "NO CAN DO"
add('h',7)
add('g', 'h')
add(5, 8)
add(2.4, 2.3)
add([2,3,4],[4,5,6])
add([2,3,4],4)
