"""
Interpreter Pattern Implementation
"""
from abc import ABC, abstractmethod
from typing import Dict


class Context:
    """Context containing global information for interpretation."""
    
    def __init__(self):
        self._variables: Dict[str, int] = {}
    
    def set_variable(self, name: str, value: int) -> None:
        """Set a variable value."""
        self._variables[name] = value
    
    def get_variable(self, name: str) -> int:
        """Get a variable value."""
        return self._variables.get(name, 0)


class Expression(ABC):
    """Abstract expression class."""
    
    @abstractmethod
    def interpret(self, context: Context) -> int:
        """Interpret the expression in the given context."""
        pass


class VariableExpression(Expression):
    """Terminal expression for variables."""
    
    def __init__(self, name: str):
        self._name = name
    
    def interpret(self, context: Context) -> int:
        return context.get_variable(self._name)


class NumberExpression(Expression):
    """Terminal expression for numbers."""
    
    def __init__(self, number: int):
        self._number = number
    
    def interpret(self, context: Context) -> int:
        return self._number


class AddExpression(Expression):
    """Non-terminal expression for addition."""
    
    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right
    
    def interpret(self, context: Context) -> int:
        return self._left.interpret(context) + self._right.interpret(context)


class SubtractExpression(Expression):
    """Non-terminal expression for subtraction."""
    
    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right
    
    def interpret(self, context: Context) -> int:
        return self._left.interpret(context) - self._right.interpret(context)


class MultiplyExpression(Expression):
    """Non-terminal expression for multiplication."""
    
    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right
    
    def interpret(self, context: Context) -> int:
        return self._left.interpret(context) * self._right.interpret(context)


if __name__ == "__main__":
    # Create context and set variables
    context = Context()
    context.set_variable("x", 10)
    context.set_variable("y", 5)
    context.set_variable("z", 2)
    
    # Build expression: (x + y) * z - 3
    # This represents: (10 + 5) * 2 - 3 = 30 - 3 = 27
    expression = SubtractExpression(
        MultiplyExpression(
            AddExpression(
                VariableExpression("x"),
                VariableExpression("y")
            ),
            VariableExpression("z")
        ),
        NumberExpression(3)
    )
    
    result = expression.interpret(context)
    print(f"Result: {result}")  # Should print 27
