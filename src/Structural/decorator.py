from functools import wraps

def make_blink(function):
	#this makes the decorator transparent in therms of its name and docstring
	@wraps(function)

	def decorator():
		#Grab the return value of the function being decorated
		ret = function()

		#Add new functionality to the function being decorated
		return "blink" + ret

	return decorator

@make_blink
def hello_world():
	"""Original"""
	return "Hello"

print(hello_world())

print(hello_world.__name__)
print(hell_world.__doc__)
