"""
Open/Closed Principle (OCP) Examples
"""
from abc import ABC, abstractmethod
from enum import Enum
from typing import List


# BAD EXAMPLE: Violates OCP - must modify existing code to add new shapes
class BadShape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        self.properties = kwargs


class BadAreaCalculator:
    """This class violates OCP - adding new shapes requires modifying this class"""
    
    def calculate_area(self, shapes: List[BadShape]) -> float:
        total_area = 0
        for shape in shapes:
            if shape.shape_type == "rectangle":
                total_area += shape.properties["width"] * shape.properties["height"]
            elif shape.shape_type == "circle":
                total_area += 3.14159 * shape.properties["radius"] ** 2
            elif shape.shape_type == "triangle":
                total_area += 0.5 * shape.properties["base"] * shape.properties["height"]
            # Adding new shapes requires modifying this method - VIOLATES OCP
        return total_area


# GOOD EXAMPLE: Follows OCP - open for extension, closed for modification
class Shape(ABC):
    """Abstract base class for all shapes"""
    
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape"""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape"""
        pass


class Rectangle(Shape):
    """Rectangle implementation - extends Shape"""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"


class Circle(Shape):
    """Circle implementation - extends Shape"""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14159 * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius
    
    def __str__(self):
        return f"Circle(radius={self.radius})"


class Triangle(Shape):
    """Triangle implementation - extends Shape"""
    
    def __init__(self, base: float, height: float, side1: float, side2: float):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    def area(self) -> float:
        return 0.5 * self.base * self.height
    
    def perimeter(self) -> float:
        return self.base + self.side1 + self.side2
    
    def __str__(self):
        return f"Triangle(base={self.base}, height={self.height})"


# New shapes can be added without modifying existing code
class Hexagon(Shape):
    """Hexagon implementation - extends Shape without modifying existing code"""
    
    def __init__(self, side: float):
        self.side = side
    
    def area(self) -> float:
        return (3 * 3**0.5 / 2) * self.side ** 2
    
    def perimeter(self) -> float:
        return 6 * self.side
    
    def __str__(self):
        return f"Hexagon(side={self.side})"


class AreaCalculator:
    """Calculator that follows OCP - doesn't need modification for new shapes"""
    
    def calculate_total_area(self, shapes: List[Shape]) -> float:
        """Calculate total area - works with any Shape implementation"""
        return sum(shape.area() for shape in shapes)
    
    def calculate_total_perimeter(self, shapes: List[Shape]) -> float:
        """Calculate total perimeter - works with any Shape implementation"""
        return sum(shape.perimeter() for shape in shapes)
    
    def get_shape_details(self, shapes: List[Shape]) -> str:
        """Get details for all shapes"""
        details = []
        for shape in shapes:
            details.append(f"{shape}: Area={shape.area():.2f}, Perimeter={shape.perimeter():.2f}")
        return "\n".join(details)


# Another OCP example: Discount strategies
class DiscountStrategy(ABC):
    """Abstract discount strategy"""
    
    @abstractmethod
    def calculate_discount(self, amount: float) -> float:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass


class NoDiscount(DiscountStrategy):
    """No discount strategy"""
    
    def calculate_discount(self, amount: float) -> float:
        return 0
    
    def get_description(self) -> str:
        return "No discount"


class PercentageDiscount(DiscountStrategy):
    """Percentage-based discount strategy"""
    
    def __init__(self, percentage: float):
        self.percentage = percentage
    
    def calculate_discount(self, amount: float) -> float:
        return amount * (self.percentage / 100)
    
    def get_description(self) -> str:
        return f"{self.percentage}% discount"


class FixedAmountDiscount(DiscountStrategy):
    """Fixed amount discount strategy"""
    
    def __init__(self, fixed_amount: float):
        self.fixed_amount = fixed_amount
    
    def calculate_discount(self, amount: float) -> float:
        return min(self.fixed_amount, amount)
    
    def get_description(self) -> str:
        return f"${self.fixed_amount} off"


# New discount strategies can be added without modifying existing code
class BuyTwoGetOneDiscount(DiscountStrategy):
    """Buy 2 get 1 free discount strategy"""
    
    def __init__(self, item_price: float):
        self.item_price = item_price
    
    def calculate_discount(self, amount: float) -> float:
        items = int(amount / self.item_price)
        free_items = items // 3
        return free_items * self.item_price
    
    def get_description(self) -> str:
        return "Buy 2 get 1 free"


class PriceCalculator:
    """Price calculator that follows OCP"""
    
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy
    
    def calculate_final_price(self, original_price: float) -> float:
        discount = self.discount_strategy.calculate_discount(original_price)
        return original_price - discount
    
    def get_price_breakdown(self, original_price: float) -> str:
        discount = self.discount_strategy.calculate_discount(original_price)
        final_price = original_price - discount
        return (f"Original: ${original_price:.2f}\n"
                f"Discount ({self.discount_strategy.get_description()}): -${discount:.2f}\n"
                f"Final: ${final_price:.2f}")


def demonstrate_ocp():
    """Demonstrate Open/Closed Principle"""
    print("=== Open/Closed Principle Demo ===\n")
    
    # Shape example
    print("1. Shape Area Calculation (extensible without modification):")
    shapes = [
        Rectangle(5, 4),
        Circle(3),
        Triangle(6, 4, 5, 5),
        Hexagon(2)  # New shape added without modifying existing code
    ]
    
    calculator = AreaCalculator()
    print(f"Total area: {calculator.calculate_total_area(shapes):.2f}")
    print(f"Total perimeter: {calculator.calculate_total_perimeter(shapes):.2f}")
    print("\nShape details:")
    print(calculator.get_shape_details(shapes))
    
    # Discount example
    print("\n2. Discount Strategies (extensible without modification):")
    original_price = 100.0
    
    discount_strategies = [
        NoDiscount(),
        PercentageDiscount(10),
        FixedAmountDiscount(15),
        BuyTwoGetOneDiscount(25)  # New strategy added without modifying existing code
    ]
    
    for strategy in discount_strategies:
        price_calc = PriceCalculator(strategy)
        print(f"\n{strategy.get_description()}:")
        print(price_calc.get_price_breakdown(original_price))
    
    print("\n3. Benefits of OCP:")
    print("- New shapes can be added without modifying AreaCalculator")
    print("- New discount strategies can be added without modifying PriceCalculator")
    print("- Existing code remains stable and tested")
    print("- Easy to extend functionality")


if __name__ == "__main__":
    demonstrate_ocp()
