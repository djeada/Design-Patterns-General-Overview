class Dog:
	"one of the objects to be returned"
	def speak(self):
		return "woof!"
	def __str__(self):
		return "Dog"

class DogFactory:
	def get_pet(self):
		"Returns dog object"
		return Dog()

	def get_food(self):
		"returns a dog food object"
		return "Dog food"

class PetStore:
	"Abstract factory"

	def __init__(self, pet_factory=None):
		"pet factory is abstract factory"
		self._pet_factory = pet_factory

	def show_pet(self):
		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is {}".format(pet))
		print("Our pet says hello by {}".format(pet.speak()))
		print("Its food is {}".format(pet_food))


#Create a concrete factory
factory = DogFactory()

#Create a pet store housing Abstract factory
shop = PetStroe(factory)

#Invoke the utility method
shop.show_pet()
