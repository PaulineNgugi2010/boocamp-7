class Animal(object):
	pass
class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def walk(self):
		return "I am walking"
class Poacher(Person):
	def __init__(self, name, age, *args, **kwargs):
		Person.__init__(self, name, age)
		self.gun = kwargs.get('gun', 'AK47')
		self.loc = kwargs.get('loc', 'Nairobi')
		self.game_park =kwargs.get('game_park' 'Tsavo')
		self.fav = kwargs.get ('fav', 'Elephant')
class Tourist(object):
	pass
p = ('Jane', 23)
#pc = ('Joe', 45, {'gun':'Rifle'}, game_park ='Amboseli', loc='Tanzania')
pc = Poacher('Pauline', 25, gun='Rifle', loc='Mombasa')
#print pc.name, pc.age, pc.walk, pc.fav pc.Poacher, pc.gun
print pc.name, pc.age, pc.gun, pc.loc