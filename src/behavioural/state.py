"""
State Pattern Implementation
"""
from abc import ABC, abstractmethod


class State(ABC):
    """Abstract state class."""
    
    @abstractmethod
    def handle_request(self, context: 'Context') -> None:
        """Handle request and potentially change state."""
        pass


class ConcreteStateA(State):
    """Concrete state A implementation."""
    
    def handle_request(self, context: 'Context') -> None:
        print("State A handling request and switching to State B")
        context.set_state(ConcreteStateB())


class ConcreteStateB(State):
    """Concrete state B implementation."""
    
    def handle_request(self, context: 'Context') -> None:
        print("State B handling request and switching to State A")
        context.set_state(ConcreteStateA())


class Context:
    """Context class that maintains state."""
    
    def __init__(self, state: State):
        self._state = state
    
    def set_state(self, state: State) -> None:
        """Change the current state."""
        print(f"Context: Transitioning to {state.__class__.__name__}")
        self._state = state
    
    def request(self) -> None:
        """Delegate request to current state."""
        self._state.handle_request(self)


if __name__ == "__main__":
    # Start with state A
    context = Context(ConcreteStateA())
    
    # Make several requests to see state transitions
    context.request()
    context.request()
    context.request()
