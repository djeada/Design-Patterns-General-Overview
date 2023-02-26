'''
In this example, ComplexFactory is an abstract factory that defines the interface for creating complex numbers. The create_complex method is a factory method that subclasses can override to create different types of complex numbers.

CartesianComplexFactory, PolarComplexFactory, and StringComplexFactory are concrete factories that create Complex objects using Cartesian, polar, and string representations, respectively.

Each factory provides its own implementation for the create_complex method, which takes different parameters depending on the representation used. The client code can use any of the concrete factories to create complex numbers in the desired representation.
'''

from math import cos, sin, pi

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
        
class ComplexFactory:
    def create_complex(self, x, y):
        pass

class CartesianComplexFactory(ComplexFactory):
    def create_complex(self, x, y):
        return Complex(x, y)
    
class PolarComplexFactory(ComplexFactory):
    def create_complex(self, r, theta):
        return Complex(r*cos(theta), r*sin(theta))
    
class StringComplexFactory(ComplexFactory):
    def create_complex(self, string):
        parts = string.split("+")
        x, y = float(parts[0]), float(parts[1][:-1])
        return Complex(x, y)
    
    
if __name__ == "__main__":
    cartesian_factory = CartesianComplexFactory()
    c1 = cartesian_factory.create_complex(1, 2)
    print(c1)
    
    polar_factory = PolarComplexFactory()
    c2 = polar_factory.create_complex(1, pi/2)
    print(c2)
    
    string_factory = StringComplexFactory()
    c3 = string_factory.create_complex("3+4i")
    print(c3)
