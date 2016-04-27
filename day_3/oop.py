from person import Person
from kenyan import Kenyan

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

k = Kenyan('Miguna', 23)
k.probe(True)
print "Is {} corrupt {}?".format(k.name, k.is_corrupt())

print Person.people_count
print p2.people_count
print b

print k.say_hello()

