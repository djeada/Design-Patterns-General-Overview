class Dog:
	def __init_(self, name):
		self._name = name
	
	def speak(self):
		return 'woof'

class Cat:
	def __init__(self, name):
		self._name = name

	def speak(self):
		return 'meow'

def get_pet(pet='dog'):
	#the facotry method

	pets = dict(dog=Dog('hope'), cat=Cat('Peace'))

	return pets[pet]

d = get_pet('dog')

print(d.speak())

c = get_pet('cat')
print(c.speak())




