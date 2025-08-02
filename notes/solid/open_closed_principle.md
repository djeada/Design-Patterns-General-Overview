# Open/Closed Principle (OCP)

## Definition
Software entities (classes, modules, functions) should be open for extension but closed for modification.

## Intent
- You should be able to extend a class's behavior without modifying its source code
- Achieve this through abstraction and polymorphism
- Protect existing code from changes when adding new functionality

## Benefits
- **Stability**: Existing code remains unchanged and stable
- **Extensibility**: Easy to add new features
- **Reduced risk**: Less chance of introducing bugs in existing functionality
- **Better design**: Encourages use of abstractions

## Example Violation
```python
# BAD: Must modify existing code to add new shapes
class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            if shape.type == "rectangle":
                total_area += shape.width * shape.height
            elif shape.type == "circle":
                total_area += 3.14 * shape.radius * shape.radius
            # Adding new shape requires modifying this method
        return total_area
```

## Good Implementation
```python
# GOOD: Open for extension, closed for modification
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class AreaCalculator:
    def calculate_area(self, shapes):
        return sum(shape.area() for shape in shapes)

# New shapes can be added without modifying existing code
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
```

## Implementation Strategies
- **Inheritance**: Extend base classes
- **Composition**: Use strategy pattern
- **Interfaces**: Define contracts for behavior
- **Dependency Injection**: Inject dependencies rather than creating them

## Common Patterns
- Strategy Pattern
- Template Method Pattern
- Decorator Pattern
- Observer Pattern
