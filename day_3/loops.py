a = [10, 50, 40, 60, 89]
for i in a:
	print i

#print in reverse

i= len(a)
print "Code 1"
while i> 0:
	print a[i-1]
	i -= 1

print "Code 2"
for x in range(len(a) - 1, -1, -1):
	print a[x]

print "Code 3_i_unpack"
b= [(2, 4), (5, 10), (6, 20), (50, 50)]
'''
x: 2, y: 4
x: 5, y: 10
'''
for i in b:
	print "x: {}, y: {}".format(*i)
print "Code 3_ii_array"
for i in b:
	print "x: {}, y: {}".format(i[0], i[1])

print "Code 3_iii_two value"

for i, j in b:
	print "x: {}, y: {}".format(i,j)

print "Three Items code-Array method"
p= [(3, 5, 6), (7, 8, 9), (8, 9,10), (90, 67, 89)]

for q in p:
	print "x: {}, y: {}, z:{}".format(q[0], q[1], q[2])