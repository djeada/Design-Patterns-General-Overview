"""
Template Method Pattern Implementation
"""
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """Abstract class defining the template method."""
    
    def template_method(self) -> None:
        """Template method defining the algorithm skeleton."""
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        self.hook1()
        self.required_operation2()
        self.base_operation3()
        self.hook2()
    
    def base_operation1(self) -> None:
        """Base operation with default implementation."""
        print("AbstractClass: I am doing the bulk of the work")
    
    def base_operation2(self) -> None:
        """Another base operation with default implementation."""
        print("AbstractClass: But I let subclasses override some operations")
    
    def base_operation3(self) -> None:
        """Yet another base operation."""
        print("AbstractClass: But I am doing the bulk of the work anyway")
    
    @abstractmethod
    def required_operation1(self) -> None:
        """Required operation that must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def required_operation2(self) -> None:
        """Another required operation."""
        pass
    
    def hook1(self) -> None:
        """Hook method that can be overridden by subclasses."""
        pass
    
    def hook2(self) -> None:
        """Another hook method."""
        pass


class ConcreteClass1(AbstractClass):
    """Concrete implementation 1."""
    
    def required_operation1(self) -> None:
        print("ConcreteClass1: Implemented Operation1")
    
    def required_operation2(self) -> None:
        print("ConcreteClass1: Implemented Operation2")


class ConcreteClass2(AbstractClass):
    """Concrete implementation 2 with hooks."""
    
    def required_operation1(self) -> None:
        print("ConcreteClass2: Implemented Operation1")
    
    def required_operation2(self) -> None:
        print("ConcreteClass2: Implemented Operation2")
    
    def hook1(self) -> None:
        print("ConcreteClass2: Overridden Hook1")


def client_code(abstract_class: AbstractClass) -> None:
    """Client code using the template method."""
    abstract_class.template_method()


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")
    
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass2())
