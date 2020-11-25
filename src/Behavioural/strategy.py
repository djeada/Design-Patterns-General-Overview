class Base:
	def __init__(self, func=None):
		if func is not None:
			self.execute = func

	def execute(self):
		print("Original execution")

	def constantFunction(self):
		print("This function won't change across derived classes")

class DerivedA(Base):
	def __init__(self):
		super().__init__(executeReplacement1)

class DerivedB(Base):
	def __init__(self):
		super().__init__(executeReplacement1)

class DerivedC(Base):
	def __init__(self):
		super().__init__(executeReplacement2)

def executeReplacement1():
    print("Execution replaced with strategy 1")

def executeReplacement2():
    print("Execution replaced with strategy 2")

if __name__ == "__main__":
    base = Base()
    childA = DerivedA()
    childB = DerivedB()
    childC = DerivedC()

    base.execute()
    childA.execute()
    childB.execute()
    childC.execute()

