# Interface Segregation Principle (ISP)

## Definition
No client should be forced to depend on methods it does not use. Many client-specific interfaces are better than one general-purpose interface.

## Intent
- Create focused, cohesive interfaces
- Avoid forcing clients to implement unnecessary methods
- Reduce coupling between classes and interfaces

## Benefits
- **Flexibility**: Clients depend only on what they need
- **Maintainability**: Changes to unused methods don't affect clients
- **Testability**: Easier to mock and test focused interfaces
- **Decoupling**: Reduces dependencies between components

## Example Violation
```python
# BAD: Fat interface forces unnecessary dependencies
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass

class HumanWorker(Worker):
    def work(self):
        print("Human working")
    
    def eat(self):
        print("Human eating")
    
    def sleep(self):
        print("Human sleeping")

class RobotWorker(Worker):
    def work(self):
        print("Robot working")
    
    def eat(self):
        # Robots don't eat - forced to implement unused method
        raise NotImplementedError("Robots don't eat")
    
    def sleep(self):
        # Robots don't sleep - forced to implement unused method  
        raise NotImplementedError("Robots don't sleep")
```

## Good Implementation
```python
# GOOD: Segregated interfaces
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class HumanWorker(Workable, Eatable, Sleepable):
    def work(self):
        print("Human working")
    
    def eat(self):
        print("Human eating")
    
    def sleep(self):
        print("Human sleeping")

class RobotWorker(Workable):
    def work(self):
        print("Robot working")

# Clients can depend on specific interfaces
class WorkManager:
    def __init__(self, worker: Workable):
        self.worker = worker
    
    def manage(self):
        self.worker.work()

class RestaurantManager:
    def __init__(self, eater: Eatable):
        self.eater = eater
    
    def serve_meal(self):
        self.eater.eat()
```

## Interface Design Guidelines
- **Role-based interfaces**: Design interfaces around client roles
- **Cohesive methods**: Group related methods together
- **Minimal interfaces**: Keep interfaces as small as possible
- **Client-specific**: Tailor interfaces to specific client needs

## Common Patterns
- **Adapter Pattern**: Adapt fat interfaces to client needs
- **Facade Pattern**: Provide simplified interface to complex subsystem
- **Strategy Pattern**: Define family of algorithms with focused interfaces

## Identification Techniques
- Look for empty or exception-throwing method implementations
- Identify clients that use only subset of interface methods
- Check for interfaces with unrelated responsibilities
- Watch for frequent interface changes affecting unrelated clients
