# Liskov Substitution Principle (LSP)

## Definition
Objects of a superclass should be replaceable with objects of its subclasses without breaking the application.

## Intent
- Subclasses should be substitutable for their base classes
- Derived classes must be substitutable for their base classes without altering program correctness
- Ensures that inheritance is used correctly

## Benefits
- **Polymorphism**: Enables true polymorphic behavior
- **Reliability**: Guarantees that subclasses work as expected
- **Maintainability**: Makes code more predictable and easier to maintain
- **Design integrity**: Ensures proper inheritance hierarchies

## Example Violation
```python
# BAD: Square violates LSP when substituted for Rectangle
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def set_width(self, width):
        self._width = width
    
    def set_height(self, height):
        self._height = height
    
    def area(self):
        return self._width * self._height

class Square(Rectangle):  # Violates LSP
    def set_width(self, width):
        self._width = width
        self._height = width  # Side effect!
    
    def set_height(self, height):
        self._width = height  # Side effect!
        self._height = height

# This breaks when Square is substituted for Rectangle
def resize_rectangle(rectangle):
    rectangle.set_width(5)
    rectangle.set_height(4)
    expected_area = 20
    actual_area = rectangle.area()
    assert actual_area == expected_area  # Fails for Square!
```

## Good Implementation
```python
# GOOD: Proper abstraction that respects LSP
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def set_width(self, width):
        self._width = width
    
    def set_height(self, height):
        self._height = height
    
    def area(self):
        return self._width * self._height

class Square(Shape):
    def __init__(self, side):
        self._side = side
    
    def set_side(self, side):
        self._side = side
    
    def area(self):
        return self._side * self._side

# Or use immutable objects
class ImmutableRectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    def area(self):
        return self._width * self._height

class ImmutableSquare(Shape):
    def __init__(self, side):
        self._side = side
    
    @property
    def side(self):
        return self._side
    
    def area(self):
        return self._side * self._side
```

## LSP Rules
- **Preconditions**: Cannot be strengthened in subclasses
- **Postconditions**: Cannot be weakened in subclasses
- **Invariants**: Must be preserved in subclasses
- **Exception types**: Subclasses should not throw new exception types

## Design Guidelines
- Use composition over inheritance when LSP would be violated
- Prefer immutable objects to avoid behavioral inconsistencies
- Design contracts carefully and document expected behavior
- Consider whether "is-a" relationship truly holds
