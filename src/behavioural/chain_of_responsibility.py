"""
Chain of Responsibility Pattern Implementation
"""
from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    """Abstract handler in the chain of responsibility."""
    
    def __init__(self):
        self._next_handler: Optional[Handler] = None
    
    def set_next(self, handler: 'Handler') -> 'Handler':
        """Set the next handler in the chain."""
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        """Handle the request or pass it to the next handler."""
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class ConcreteHandlerA(Handler):
    """Concrete handler that handles requests starting with 'A'."""
    
    def handle(self, request: str) -> Optional[str]:
        if request.startswith('A'):
            return f"HandlerA processed: {request}"
        return super().handle(request)


class ConcreteHandlerB(Handler):
    """Concrete handler that handles requests starting with 'B'."""
    
    def handle(self, request: str) -> Optional[str]:
        if request.startswith('B'):
            return f"HandlerB processed: {request}"
        return super().handle(request)


class ConcreteHandlerC(Handler):
    """Concrete handler that handles requests starting with 'C'."""
    
    def handle(self, request: str) -> Optional[str]:
        if request.startswith('C'):
            return f"HandlerC processed: {request}"
        return super().handle(request)


def client_code(handler: Handler) -> None:
    """Client code that uses the chain."""
    requests = ["Apple", "Banana", "Cherry", "Diamond"]
    
    for request in requests:
        result = handler.handle(request)
        if result:
            print(result)
        else:
            print(f"No handler found for: {request}")


if __name__ == "__main__":
    # Build the chain
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_c = ConcreteHandlerC()
    
    handler_a.set_next(handler_b).set_next(handler_c)
    
    # Test the chain
    client_code(handler_a)
