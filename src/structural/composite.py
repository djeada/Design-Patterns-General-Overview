"""
Composite Pattern Implementation
"""
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """Abstract component class."""
    
    @abstractmethod
    def operation(self) -> str:
        """Perform the operation."""
        pass
    
    def add(self, component: 'Component') -> None:
        """Add a child component (only for composites)."""
        raise NotImplementedError
    
    def remove(self, component: 'Component') -> None:
        """Remove a child component (only for composites)."""
        raise NotImplementedError
    
    def is_composite(self) -> bool:
        """Check if this is a composite."""
        return False


class Leaf(Component):
    """Leaf component (no children)."""
    
    def __init__(self, name: str):
        self.name = name
    
    def operation(self) -> str:
        return f"Leaf({self.name})"


class Composite(Component):
    """Composite component (can have children)."""
    
    def __init__(self, name: str):
        self.name = name
        self._children: List[Component] = []
    
    def add(self, component: Component) -> None:
        """Add a child component."""
        self._children.append(component)
    
    def remove(self, component: Component) -> None:
        """Remove a child component."""
        self._children.remove(component)
    
    def is_composite(self) -> bool:
        return True
    
    def operation(self) -> str:
        """Perform operation on all children."""
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({self.name})[{'+'.join(results)}]"


def client_code(component: Component) -> None:
    """Client code that works with components."""
    print(f"RESULT: {component.operation()}")


def client_code2(component1: Component, component2: Component) -> None:
    """Client code demonstrating dynamic composition."""
    if component1.is_composite():
        component1.add(component2)
    
    print(f"RESULT: {component1.operation()}")


if __name__ == "__main__":
    # Simple leaf
    simple = Leaf("Simple")
    print("Client: I've got a simple component:")
    client_code(simple)
    print()
    
    # Complex tree
    tree = Composite("Root")
    branch1 = Composite("Branch1")
    branch1.add(Leaf("Leaf1"))
    branch1.add(Leaf("Leaf2"))
    
    branch2 = Composite("Branch2")
    branch2.add(Leaf("Leaf3"))
    
    tree.add(branch1)
    tree.add(branch2)
    
    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print()
    
    # Dynamic composition
    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)
