class Component(object):
	#Abstrac class
	def __init__(self, *args, **kwargs):
		pass

	def component_function(self):
		pass

class Child(Component):
	#Concrete class
	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)

		self.name = args[0]
	
	def component_function(self):
		print(self.name)

class Composite():
	#Concrete class and maintains the tree recursive structure

	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)
		#we store the composite object
		self.name = args[0]

		#here we keep child items
		self.children = []


	def append_child(self, child):
		self.children.append(child)

	def remove_child(self, child):
		self.children.remove(child)

	def component_function(self):
		print(self.name)
		for i in self.children:
			i.component_function()

sub1 = Compoite('submenu1')
sub11 = Child('submenu11')
sub12 = Child('submenu12')

sub1.append_child(sub11)
sub1.append_child(sub12)

top = composite('top menu')

sub2 = Child('submenu2')
top.append_child(sub1)
top.apend_child(sub2)

top.component_function()
