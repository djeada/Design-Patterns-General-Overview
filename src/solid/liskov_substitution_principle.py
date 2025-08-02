"""
Liskov Substitution Principle (LSP) Examples
"""
from abc import ABC, abstractmethod
from typing import List


# BAD EXAMPLE: Violates LSP
class BadRectangle:
    """Rectangle class that will be problematic when subclassed"""
    
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    
    def set_width(self, width: float):
        self._width = width
    
    def set_height(self, height: float):
        self._height = height
    
    def get_width(self) -> float:
        return self._width
    
    def get_height(self) -> float:
        return self._height
    
    def area(self) -> float:
        return self._width * self._height


class BadSquare(BadRectangle):
    """Square class that violates LSP when substituted for Rectangle"""
    
    def __init__(self, side: float):
        super().__init__(side, side)
    
    def set_width(self, width: float):
        # Violates LSP: Changes both width and height when only width should change
        self._width = width
        self._height = width  # Side effect that breaks Rectangle's contract
    
    def set_height(self, height: float):
        # Violates LSP: Changes both width and height when only height should change
        self._width = height  # Side effect that breaks Rectangle's contract
        self._height = height


def problematic_function(rectangle: BadRectangle):
    """This function expects Rectangle behavior but breaks with BadSquare"""
    rectangle.set_width(5)
    rectangle.set_height(4)
    expected_area = 20  # 5 * 4
    actual_area = rectangle.area()
    
    print(f"Expected area: {expected_area}, Actual area: {actual_area}")
    
    # This assertion will fail for BadSquare because it changes both dimensions
    # when setting width or height, resulting in area = 4 * 4 = 16
    if actual_area != expected_area:
        print("❌ LSP Violation: Square doesn't behave like Rectangle!")
        return False
    else:
        print("✅ Behaves correctly as Rectangle")
        return True


# GOOD EXAMPLE: Follows LSP using proper abstraction
class Shape(ABC):
    """Abstract base class for all shapes"""
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        pass


class Rectangle(Shape):
    """Rectangle implementation following LSP"""
    
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self._width = width
        self._height = height
    
    def get_width(self) -> float:
        return self._width
    
    def get_height(self) -> float:
        return self._height
    
    def area(self) -> float:
        return self._width * self._height
    
    def __str__(self) -> str:
        return f"Rectangle({self._width}x{self._height})"


class Square(Shape):
    """Square implementation following LSP"""
    
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Side must be positive")
        self._side = side
    
    def get_side(self) -> float:
        return self._side
    
    def area(self) -> float:
        return self._side * self._side
    
    def __str__(self) -> str:
        return f"Square({self._side}x{self._side})"


# Alternative approach: Immutable shapes
class ImmutableRectangle(Shape):
    """Immutable rectangle that follows LSP"""
    
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self._width = width
        self._height = height
    
    @property
    def width(self) -> float:
        return self._width
    
    @property
    def height(self) -> float:
        return self._height
    
    def with_width(self, width: float) -> 'ImmutableRectangle':
        """Return new rectangle with different width"""
        return ImmutableRectangle(width, self._height)
    
    def with_height(self, height: float) -> 'ImmutableRectangle':
        """Return new rectangle with different height"""
        return ImmutableRectangle(self._width, height)
    
    def area(self) -> float:
        return self._width * self._height
    
    def __str__(self) -> str:
        return f"ImmutableRectangle({self._width}x{self._height})"


class ImmutableSquare(Shape):
    """Immutable square that follows LSP"""
    
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Side must be positive")
        self._side = side
    
    @property
    def side(self) -> float:
        return self._side
    
    def with_side(self, side: float) -> 'ImmutableSquare':
        """Return new square with different side"""
        return ImmutableSquare(side)
    
    def area(self) -> float:
        return self._side * self._side
    
    def __str__(self) -> str:
        return f"ImmutableSquare({self._side}x{self._side})"


# Another LSP example: Bird hierarchy
class Bird(ABC):
    """Abstract bird class"""
    
    @abstractmethod
    def eat(self) -> str:
        pass
    
    @abstractmethod
    def make_sound(self) -> str:
        pass


class FlyingBird(Bird):
    """Abstract class for birds that can fly"""
    
    @abstractmethod
    def fly(self) -> str:
        pass


class Sparrow(FlyingBird):
    """Sparrow implementation"""
    
    def eat(self) -> str:
        return "Sparrow is eating seeds"
    
    def make_sound(self) -> str:
        return "Chirp chirp!"
    
    def fly(self) -> str:
        return "Sparrow is flying high!"


class Eagle(FlyingBird):
    """Eagle implementation"""
    
    def eat(self) -> str:
        return "Eagle is hunting for prey"
    
    def make_sound(self) -> str:
        return "Screech!"
    
    def fly(self) -> str:
        return "Eagle is soaring majestically!"


class Penguin(Bird):
    """Penguin implementation - cannot fly, so doesn't inherit from FlyingBird"""
    
    def eat(self) -> str:
        return "Penguin is eating fish"
    
    def make_sound(self) -> str:
        return "Squawk!"
    
    def swim(self) -> str:
        return "Penguin is swimming gracefully!"


class BirdHandler:
    """Handles birds following LSP"""
    
    def handle_bird(self, bird: Bird) -> str:
        """Can work with any Bird implementation"""
        result = f"{bird.make_sound()}\n{bird.eat()}"
        return result
    
    def handle_flying_birds(self, birds: List[FlyingBird]) -> str:
        """Can work with any FlyingBird implementation"""
        results = []
        for bird in birds:
            results.append(f"{bird.make_sound()}\n{bird.fly()}")
        return "\n---\n".join(results)


def demonstrate_lsp():
    """Demonstrate Liskov Substitution Principle"""
    print("=== Liskov Substitution Principle Demo ===\n")
    
    # Bad example - LSP violation
    print("1. LSP Violation Example:")
    print("Testing BadRectangle:")
    bad_rect = BadRectangle(3, 4)
    problematic_function(bad_rect)
    
    print("\nTesting BadSquare (should violate LSP):")
    bad_square = BadSquare(3)
    problematic_function(bad_square)
    
    # Good example - LSP compliance
    print("\n2. LSP Compliant Example:")
    shapes: List[Shape] = [
        Rectangle(5, 4),
        Square(3),
        ImmutableRectangle(6, 2),
        ImmutableSquare(4)
    ]
    
    print("All shapes can be used polymorphically:")
    for shape in shapes:
        print(f"{shape}: Area = {shape.area()}")
    
    # Bird example
    print("\n3. Bird Hierarchy (LSP Compliant):")
    bird_handler = BirdHandler()
    
    all_birds: List[Bird] = [Sparrow(), Eagle(), Penguin()]
    print("Handling all birds:")
    for bird in all_birds:
        print(f"--- {bird.__class__.__name__} ---")
        print(bird_handler.handle_bird(bird))
    
    flying_birds: List[FlyingBird] = [Sparrow(), Eagle()]
    print("\nHandling only flying birds:")
    print(bird_handler.handle_flying_birds(flying_birds))
    
    print("\n4. LSP Benefits:")
    print("- Subclasses can be substituted for base classes")
    print("- Polymorphism works correctly")
    print("- Client code doesn't need to know specific types")
    print("- Inheritance hierarchies are reliable and predictable")


if __name__ == "__main__":
    demonstrate_lsp()
