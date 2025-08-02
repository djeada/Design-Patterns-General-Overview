# Dependency Inversion Principle (DIP)

## Definition
1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.

## Intent
- Invert the direction of dependencies
- Depend on abstractions, not concretions
- Enable flexibility and testability through dependency injection

## Benefits
- **Flexibility**: Easy to swap implementations
- **Testability**: Can inject mock dependencies for testing
- **Maintainability**: Changes in low-level modules don't affect high-level modules
- **Reusability**: High-level modules can work with different implementations

## Example Violation
```python
# BAD: High-level module depends on low-level module
class MySQLDatabase:
    def save(self, data):
        print(f"Saving {data} to MySQL database")

class UserService:  # High-level module
    def __init__(self):
        self.database = MySQLDatabase()  # Direct dependency on low-level module
    
    def create_user(self, user_data):
        # Business logic
        processed_data = self.process_user_data(user_data)
        # Depends on concrete implementation
        self.database.save(processed_data)
    
    def process_user_data(self, user_data):
        return f"processed_{user_data}"
```

## Good Implementation
```python
# GOOD: Both depend on abstraction
from abc import ABC, abstractmethod

# Abstraction
class DatabaseInterface(ABC):
    @abstractmethod
    def save(self, data):
        pass

# Low-level modules depend on abstraction
class MySQLDatabase(DatabaseInterface):
    def save(self, data):
        print(f"Saving {data} to MySQL database")

class PostgreSQLDatabase(DatabaseInterface):
    def save(self, data):
        print(f"Saving {data} to PostgreSQL database")

class MongoDatabase(DatabaseInterface):
    def save(self, data):
        print(f"Saving {data} to MongoDB")

# High-level module depends on abstraction
class UserService:
    def __init__(self, database: DatabaseInterface):
        self.database = database  # Depends on abstraction
    
    def create_user(self, user_data):
        processed_data = self.process_user_data(user_data)
        self.database.save(processed_data)
    
    def process_user_data(self, user_data):
        return f"processed_{user_data}"

# Dependency injection
def main():
    # Can easily switch database implementations
    mysql_db = MySQLDatabase()
    user_service = UserService(mysql_db)
    user_service.create_user("John Doe")
    
    # Switch to different database without changing UserService
    postgres_db = PostgreSQLDatabase()
    user_service2 = UserService(postgres_db)
    user_service2.create_user("Jane Smith")
```

## Implementation Techniques

### 1. Constructor Injection
```python
class OrderService:
    def __init__(self, payment_processor: PaymentProcessorInterface,
                 email_service: EmailServiceInterface):
        self.payment_processor = payment_processor
        self.email_service = email_service
```

### 2. Setter Injection
```python
class OrderService:
    def set_payment_processor(self, processor: PaymentProcessorInterface):
        self.payment_processor = processor
    
    def set_email_service(self, service: EmailServiceInterface):
        self.email_service = service
```

### 3. Interface Injection
```python
class PaymentProcessorProvider(ABC):
    @abstractmethod
    def provide_payment_processor(self) -> PaymentProcessorInterface:
        pass
```

## Dependency Injection Container Example
```python
class DIContainer:
    def __init__(self):
        self._services = {}
        self._singletons = {}
    
    def register(self, interface, implementation, singleton=False):
        self._services[interface] = (implementation, singleton)
    
    def resolve(self, interface):
        if interface not in self._services:
            raise ValueError(f"Service {interface} not registered")
        
        implementation, is_singleton = self._services[interface]
        
        if is_singleton:
            if interface not in self._singletons:
                self._singletons[interface] = implementation()
            return self._singletons[interface]
        
        return implementation()

# Usage
container = DIContainer()
container.register(DatabaseInterface, MySQLDatabase, singleton=True)
container.register(EmailServiceInterface, SMTPEmailService)

database = container.resolve(DatabaseInterface)
user_service = UserService(database)
```

## Benefits in Testing
```python
import unittest
from unittest.mock import Mock

class TestUserService(unittest.TestCase):
    def test_create_user(self):
        # Mock dependency
        mock_database = Mock(spec=DatabaseInterface)
        user_service = UserService(mock_database)
        
        user_service.create_user("test_user")
        
        # Verify interaction with dependency
        mock_database.save.assert_called_once_with("processed_test_user")
```

## Common Anti-patterns
- **Service Locator**: Hides dependencies instead of making them explicit
- **Static Dependencies**: Using static methods/classes directly
- **New Operator**: Creating dependencies directly with `new` or constructor calls
- **Concrete Inheritance**: Inheriting from concrete classes instead of abstractions
