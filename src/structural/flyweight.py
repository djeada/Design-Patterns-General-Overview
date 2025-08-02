"""
Flyweight Pattern Implementation
"""
from typing import Dict


class Flyweight:
    """Flyweight class storing intrinsic state."""
    
    def __init__(self, intrinsic_state: str):
        self._intrinsic_state = intrinsic_state
    
    def operation(self, extrinsic_state: str) -> None:
        """Operation using both intrinsic and extrinsic state."""
        print(f"Flyweight: Displaying intrinsic ({self._intrinsic_state}) "
              f"and extrinsic ({extrinsic_state}) state.")


class FlyweightFactory:
    """Factory for managing flyweight instances."""
    
    def __init__(self):
        self._flyweights: Dict[str, Flyweight] = {}
    
    def get_flyweight(self, intrinsic_state: str) -> Flyweight:
        """Get a flyweight instance, creating if necessary."""
        if intrinsic_state not in self._flyweights:
            print(f"FlyweightFactory: Creating flyweight for '{intrinsic_state}'")
            self._flyweights[intrinsic_state] = Flyweight(intrinsic_state)
        else:
            print(f"FlyweightFactory: Reusing existing flyweight for '{intrinsic_state}'")
        
        return self._flyweights[intrinsic_state]
    
    def list_flyweights(self) -> None:
        """List all created flyweights."""
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        for key in self._flyweights.keys():
            print(f"  - {key}")


class Context:
    """Context class storing extrinsic state and flyweight reference."""
    
    def __init__(self, flyweight: Flyweight, extrinsic_state: str):
        self._flyweight = flyweight
        self._extrinsic_state = extrinsic_state
    
    def operation(self) -> None:
        """Delegate operation to flyweight with extrinsic state."""
        self._flyweight.operation(self._extrinsic_state)


def add_car_to_police_database(
    factory: FlyweightFactory, 
    plates: str, 
    owner: str, 
    brand: str, 
    model: str, 
    color: str
) -> None:
    """Add a car to the police database using flyweight pattern."""
    print("\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight(f"{brand}-{model}-{color}")
    # Context stores extrinsic state (plates, owner)
    context = Context(flyweight, f"{plates}-{owner}")
    context.operation()


if __name__ == "__main__":
    factory = FlyweightFactory()
    
    # Add cars to police database
    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red"
    )
    
    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red"
    )
    
    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red"  # Same flyweight as first
    )
    
    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X6", "blue"
    )
    
    print("\n")
    factory.list_flyweights()
