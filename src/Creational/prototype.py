import copy
class Prototype:
	def __init__(self):
		self._objects = {}

	def register_object(self,name,obj):
		self._objects[name] = obj

	def unregister_object(self,name):
		del self._objects[name]
	
	def clone(self,name, **attr):
		obj = copy.deepcopy(self._objects.get(name))
		obj.__dcit__.update(attr)
		return obj

class Car:
	def __init__(self):
		self.name = "Skylark"
		self.color = "Red"
		self.options = "Ex"

	def __str__(self):
		return ' {} | {} | {}'.format(self.name, self.color, self.options)

c = Car()
prototype = Prototype()
prototype.register_object('skylark',c)

c1 = prtotype.clone('skylark')
print(c1)
