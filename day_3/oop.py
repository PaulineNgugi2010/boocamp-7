class Person:
	# class variable
	people_count = 0
	def __init__(self, name,age):
		self.name = name
		self.age = age
		Person.people_count += 1
	def __repr__(self):
		return "<object:{} and {}>".format(self.name, self.age)

	def say_hello(self):
		return "Hello, I'm {} and {} y/o".format(self.name, self.age)
p = Person('Joe', 23)
p2 = Person('Jane', 23)
p3 = Person('George', 40)
print p.say_hello()
a = [('Jane', 23), ('Joe', 34), ('Jacob', 23), ('Jee', 18), ('Josh', 60)]
b = []




for name, age in a:
	person = Person(name, age)
	b.append(person)

for item in b:
	print item.say_hello()
print Person.people_count
print p2.people_count
print b
