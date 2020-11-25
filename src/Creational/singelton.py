class Borg:
	"making class attributes global"
	_shared_state = {} #attribute dictionary
	
	def __init__(self):
		self.__dict__ = self._shared_state

class Singelton(Borg):
	#This class shares all its attributes among its various instances

	def __init(self, **kwargs):
		Borg.__init__(self)
		self._shared_state.update(kwargs)

	def __str__(self):
		#returns the attribute dictionary for printing
	return str(self._shared_state)

#Let's create a singelton object and add acronym

x = Singelton(HTTP = "Hyper Text Transfer Proocol")
print(x)
y = Singelton(SNMP = "Simple Network Management Protocol")
print(y)
