"""
Prototype Pattern Implementation
"""
import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    """Abstract prototype class."""
    
    @abstractmethod
    def clone(self) -> 'Prototype':
        """Clone the prototype."""
        pass


class ConcretePrototype1(Prototype):
    """Concrete prototype implementation 1."""
    
    def __init__(self, value: str):
        self.value = value
        self.list_data = [1, 2, 3]
    
    def clone(self) -> 'ConcretePrototype1':
        """Create a deep copy of the prototype."""
        return copy.deepcopy(self)
    
    def __str__(self) -> str:
        return f"ConcretePrototype1(value={self.value}, list_data={self.list_data})"


class ConcretePrototype2(Prototype):
    """Concrete prototype implementation 2."""
    
    def __init__(self, number: int):
        self.number = number
        self.nested_object = {"key": "value"}
    
    def clone(self) -> 'ConcretePrototype2':
        """Create a deep copy of the prototype."""
        return copy.deepcopy(self)
    
    def __str__(self) -> str:
        return f"ConcretePrototype2(number={self.number}, nested_object={self.nested_object})"


class PrototypeRegistry:
    """Registry to manage prototypes."""
    
    def __init__(self):
        self._prototypes = {}
    
    def register_prototype(self, name: str, prototype: Prototype) -> None:
        """Register a prototype."""
        self._prototypes[name] = prototype
    
    def create(self, name: str) -> Prototype:
        """Create a new instance by cloning the registered prototype."""
        prototype = self._prototypes.get(name)
        if prototype:
            return prototype.clone()
        raise ValueError(f"Prototype '{name}' not found")


if __name__ == "__main__":
    # Create prototypes
    prototype1 = ConcretePrototype1("original")
    prototype2 = ConcretePrototype2(42)
    
    # Register prototypes
    registry = PrototypeRegistry()
    registry.register_prototype("type1", prototype1)
    registry.register_prototype("type2", prototype2)
    
    # Create clones
    clone1 = registry.create("type1")
    clone2 = registry.create("type2")
    
    # Modify clones to show they are independent
    clone1.value = "cloned"
    clone1.list_data.append(4)
    
    clone2.number = 100
    clone2.nested_object["key"] = "modified"
    
    # Display results
    print("Original prototypes:")
    print(prototype1)
    print(prototype2)
    print("\nCloned objects:")
    print(clone1)
    print(clone2)
