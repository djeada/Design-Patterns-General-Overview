# Single Responsibility Principle (SRP)

## Definition
A class should have only one reason to change, meaning it should have only one job or responsibility.

## Intent
- Each class should focus on a single functionality
- Changes to one aspect of the software should affect only one class
- Promotes high cohesion and low coupling

## Benefits
- **Maintainability**: Easier to understand and modify
- **Testability**: Simpler to write unit tests
- **Reusability**: Classes with single responsibilities are more reusable
- **Reduced coupling**: Dependencies between classes are minimized

## Example Violations
```python
# BAD: Multiple responsibilities
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def save_to_database(self):  # Database responsibility
        pass
    
    def send_email(self):  # Email responsibility
        pass
    
    def generate_report(self):  # Reporting responsibility
        pass
```

## Good Implementation
```python
# GOOD: Single responsibility per class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        pass

class EmailService:
    def send_email(self, user, message):
        pass

class ReportGenerator:
    def generate_user_report(self, user):
        pass
```

## Key Questions to Ask
- Does this class have more than one reason to change?
- Can I describe what this class does without using "and" or "or"?
- Would changes to different features require modifying this class?

## Common Anti-patterns
- **God Class**: Classes that know too much or do too much
- **Swiss Army Knife**: Classes with many unrelated methods
- **Kitchen Sink**: Classes that accumulate functionality over time
