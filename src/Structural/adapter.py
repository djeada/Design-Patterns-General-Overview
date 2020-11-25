class Korean:
	def __init__(self):
		self.name = 'Korean'
	def speak_korean(self):
		print(self.name + ' speaks korean.')

class British:
	def __init__(self):
		self.name = 'British'		

	def speak_english(self):
		print(self.name + ' speaks english.')

class Algerian:
	def __init__(self):
		self.name = 'Algerian'
	
	def speak_arabic(self):
		print(self.name + ' speaks arabic.')

class Adapter:
	def __init__(self, object, **adapted_method):
		self._object = object

		#add a new dictionary item that establishes the mapping between 
		#generic and concrete methods 
		self.__dict__.update(adapted_method)

	def __getattr(self,attr):
		return getattr(self._object, attr)

if __name__ == "__main__":

	korean = Korean()
	british = British()
	algerian = Algerian()

	adaptedKorean = Adapter(korean, speak=korean.speak_korean)
	adaptedBritish = Adapter(british, speak=british.speak_english)
	adaptedAlgerian = Adapter(algerian, speak=algerian.speak_arabic)

	adaptedKorean.speak()
	adaptedBritish.speak()
	adaptedAlgerian.speak()
