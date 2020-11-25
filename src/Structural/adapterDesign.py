class Korean:
	def __init__(self):
		self.name = 'Korean'
	def speak_korean(self):
		return "korean"

class British:
	def __init__(self):
		self.name = 'British'		

	def speak_english(self):
		return 'british'

class Adapter:
	def __init__(self, object, **adapted_method):
		self._object = object

		#add a new dictionary item betaht establishes the mapping between the generic method name: speak() and the concrete method 
		self.__dict__.update(adapted_method)

	def __getattr(self,attr):
		return getattr(self._object, attr)

#List to store speaker objects
objects = []

korean = Korean()
british = British()

objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
	print('{} says {}'.format(obj.name,obj.speak()))
