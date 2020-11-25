class Borg:
	_shared_state = {}
	
	def __init__(self):
		self.__dict__ = self._shared_state

#This class shares all its attributes among its various instances
class Singelton(Borg):
	def __init__(self, **kwargs):
		Borg.__init__(self)
		self._shared_state.update(kwargs)

	def __str__(self):
		return str(self._shared_state)

if __name__ == "__main__":
	x = Singelton(HTTP="Hyper Text Transfer Proocol")
	y = Singelton(SNMP="Simple Network Management Protocol")

	print(x)
	print(y)
