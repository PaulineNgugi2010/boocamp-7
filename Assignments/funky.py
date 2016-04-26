def funky(a, b):

  	if isinstance(a, (int,list,float)) and isinstance (b, (int,list,float)):
		return a + b
	elif isinstance(a, dict) and isinstance (b, dict):
		z = dict(a.items() + b.items())
		return z
	elif type(a) ==str or type(b) ==str:
		return str(a) + str(b)

	else:
		return "NO CAN DO"
print('h',7)
print funky('g', 'h')
print funky(5, 8)
print funky(2.4, 2.3)
print funky({1: ""}, {0: "g"})
print funky([2,3,4],[4,5,6])
