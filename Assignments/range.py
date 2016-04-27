def range_(x='', y='', z=''):

	'''
	f = [(10, 20, 40), (10, 40), (4, 5, 20)]

	x: 10, y: 40, z:40
	x: 10, y: 20
	x: 4, y: 5, z= 20
	'''
	'''if x == False:
		return "y: {} and z: {}".format(y,z)

	elif y ==False:
		return "x: {} and z: {}".format(x,z)'''

	if z ==False:
		return "x: {} and y: {}".format(x,y)
	else:
		return "x: {} and y: {}, z: {}".format(x,y,z)


f = [(10, 40), (10, 40), (4, 5, 20)]

for item in f:
	print range_(*item)

