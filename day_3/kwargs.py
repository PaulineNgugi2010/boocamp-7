def hello_again(**kwargs):
	return "I am {}, and am I'm {}".format(kwargs['name'], kwargs ['age'])
print hello_again(name='Joe', age=20)
print hello_again(age=20, name='Jane')

other_people = [
			{'name': 'Joe', 'age':98},
			{'name': 'Jane', 'age':60}, 
			{'name': 'Pauline', 'age':26} 

	]
Pauline = {'name': 'Joe', 'age':98}

print hello_again(**Pauline)

for person in other_people:
	hello_again(**person)

