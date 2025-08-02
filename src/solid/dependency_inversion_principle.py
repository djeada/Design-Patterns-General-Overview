"""
Dependency Inversion Principle (DIP) Examples
"""
from abc import ABC, abstractmethod
from typing import List, Dict


# BAD EXAMPLE: High-level module depends on low-level module (violates DIP)
class BadMySQLDatabase:
    """Low-level module - concrete database implementation"""
    
    def save_user(self, user_data: dict):
        print(f"Saving {user_data} to MySQL database")
        # MySQL-specific implementation
    
    def get_user(self, user_id: int) -> dict:
        print(f"Getting user {user_id} from MySQL database")
        return {"id": user_id, "name": "John", "email": "john@example.com"}


class BadEmailService:
    """Low-level module - concrete email service"""
    
    def send_email(self, to: str, subject: str, body: str):
        print(f"Sending email to {to}: {subject}")
        # SMTP-specific implementation


class BadUserService:
    """High-level module that violates DIP by depending on concrete classes"""
    
    def __init__(self):
        # Direct dependencies on low-level modules - VIOLATES DIP
        self.database = BadMySQLDatabase()
        self.email_service = BadEmailService()
    
    def register_user(self, user_data: dict):
        # High-level business logic
        validated_data = self.validate_user_data(user_data)
        
        # Depends on concrete implementation - hard to test and change
        self.database.save_user(validated_data)
        self.email_service.send_email(
            validated_data["email"],
            "Welcome!",
            "Welcome to our service!"
        )
    
    def validate_user_data(self, user_data: dict) -> dict:
        # Business logic for validation
        return user_data


# GOOD EXAMPLE: Both high-level and low-level modules depend on abstractions
class DatabaseInterface(ABC):
    """Abstraction for database operations"""
    
    @abstractmethod
    def save_user(self, user_data: dict) -> bool:
        pass
    
    @abstractmethod
    def get_user(self, user_id: int) -> dict:
        pass
    
    @abstractmethod
    def get_all_users(self) -> List[dict]:
        pass


class EmailServiceInterface(ABC):
    """Abstraction for email operations"""
    
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> bool:
        pass


class LoggerInterface(ABC):
    """Abstraction for logging operations"""
    
    @abstractmethod
    def log(self, message: str, level: str = "INFO") -> None:
        pass


# Low-level modules implementing abstractions
class MySQLDatabase(DatabaseInterface):
    """MySQL implementation of database interface"""
    
    def __init__(self):
        self.users = {}  # Simulate database
        self.next_id = 1
    
    def save_user(self, user_data: dict) -> bool:
        user_id = self.next_id
        self.next_id += 1
        user_data["id"] = user_id
        self.users[user_id] = user_data
        print(f"MySQL: Saved user {user_data['name']} with ID {user_id}")
        return True
    
    def get_user(self, user_id: int) -> dict:
        user = self.users.get(user_id, {})
        print(f"MySQL: Retrieved user {user_id}")
        return user
    
    def get_all_users(self) -> List[dict]:
        return list(self.users.values())


class PostgreSQLDatabase(DatabaseInterface):
    """PostgreSQL implementation of database interface"""
    
    def __init__(self):
        self.users = []  # Simulate database
    
    def save_user(self, user_data: dict) -> bool:
        user_data["id"] = len(self.users) + 1
        self.users.append(user_data)
        print(f"PostgreSQL: Saved user {user_data['name']} with ID {user_data['id']}")
        return True
    
    def get_user(self, user_id: int) -> dict:
        for user in self.users:
            if user["id"] == user_id:
                print(f"PostgreSQL: Retrieved user {user_id}")
                return user
        return {}
    
    def get_all_users(self) -> List[dict]:
        return self.users.copy()


class MongoDatabase(DatabaseInterface):
    """MongoDB implementation of database interface"""
    
    def __init__(self):
        self.users = {}  # Simulate MongoDB collection
        self.counter = 1
    
    def save_user(self, user_data: dict) -> bool:
        doc_id = f"user_{self.counter}"
        self.counter += 1
        user_data["_id"] = doc_id
        self.users[doc_id] = user_data
        print(f"MongoDB: Saved user {user_data['name']} with ID {doc_id}")
        return True
    
    def get_user(self, user_id: int) -> dict:
        doc_id = f"user_{user_id}"
        user = self.users.get(doc_id, {})
        print(f"MongoDB: Retrieved user {doc_id}")
        return user
    
    def get_all_users(self) -> List[dict]:
        return list(self.users.values())


class SMTPEmailService(EmailServiceInterface):
    """SMTP implementation of email service"""
    
    def send_email(self, to: str, subject: str, body: str) -> bool:
        print(f"SMTP: Sending email to {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        return True


class SendGridEmailService(EmailServiceInterface):
    """SendGrid implementation of email service"""
    
    def send_email(self, to: str, subject: str, body: str) -> bool:
        print(f"SendGrid API: Sending email to {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        return True


class ConsoleLogger(LoggerInterface):
    """Console implementation of logger"""
    
    def log(self, message: str, level: str = "INFO") -> None:
        print(f"[{level}] {message}")


class FileLogger(LoggerInterface):
    """File implementation of logger"""
    
    def __init__(self, filename: str):
        self.filename = filename
    
    def log(self, message: str, level: str = "INFO") -> None:
        print(f"File({self.filename}) [{level}] {message}")


# High-level module depending on abstractions
class UserService:
    """High-level module following DIP - depends on abstractions"""
    
    def __init__(self, database: DatabaseInterface, 
                 email_service: EmailServiceInterface,
                 logger: LoggerInterface):
        # Depends on abstractions, not concrete implementations
        self.database = database
        self.email_service = email_service
        self.logger = logger
    
    def register_user(self, user_data: dict) -> bool:
        """Register a new user - high-level business logic"""
        try:
            self.logger.log(f"Registering user: {user_data.get('name')}")
            
            # High-level business logic
            validated_data = self.validate_user_data(user_data)
            
            # Use abstractions - implementation details are hidden
            success = self.database.save_user(validated_data)
            
            if success:
                self.email_service.send_email(
                    validated_data["email"],
                    "Welcome to Our Service!",
                    f"Hello {validated_data['name']}, welcome to our platform!"
                )
                self.logger.log(f"Successfully registered user: {validated_data['name']}")
                return True
            else:
                self.logger.log(f"Failed to save user: {validated_data['name']}", "ERROR")
                return False
                
        except Exception as e:
            self.logger.log(f"Error registering user: {str(e)}", "ERROR")
            return False
    
    def get_user_by_id(self, user_id: int) -> dict:
        """Get user by ID"""
        self.logger.log(f"Retrieving user with ID: {user_id}")
        return self.database.get_user(user_id)
    
    def get_all_users(self) -> List[dict]:
        """Get all users"""
        self.logger.log("Retrieving all users")
        return self.database.get_all_users()
    
    def validate_user_data(self, user_data: dict) -> dict:
        """Validate user data - business logic"""
        if not user_data.get("name"):
            raise ValueError("Name is required")
        if not user_data.get("email"):
            raise ValueError("Email is required")
        if "@" not in user_data.get("email", ""):
            raise ValueError("Invalid email format")
        
        return user_data.copy()


# Dependency Injection Container
class DIContainer:
    """Simple dependency injection container"""
    
    def __init__(self):
        self._services: Dict[type, object] = {}
        self._factories: Dict[type, callable] = {}
    
    def register_instance(self, interface: type, instance: object):
        """Register a singleton instance"""
        self._services[interface] = instance
    
    def register_factory(self, interface: type, factory: callable):
        """Register a factory function"""
        self._factories[interface] = factory
    
    def resolve(self, interface: type):
        """Resolve a service instance"""
        if interface in self._services:
            return self._services[interface]
        elif interface in self._factories:
            return self._factories[interface]()
        else:
            raise ValueError(f"Service {interface.__name__} not registered")


def demonstrate_dip():
    """Demonstrate Dependency Inversion Principle"""
    print("=== Dependency Inversion Principle Demo ===\n")
    
    # Configuration 1: MySQL + SMTP + Console Logger
    print("1. Configuration 1: MySQL + SMTP + Console Logger")
    mysql_db = MySQLDatabase()
    smtp_email = SMTPEmailService()
    console_logger = ConsoleLogger()
    
    user_service1 = UserService(mysql_db, smtp_email, console_logger)
    user_service1.register_user({"name": "Alice", "email": "alice@example.com"})
    
    print("\n" + "="*50)
    
    # Configuration 2: PostgreSQL + SendGrid + File Logger
    print("\n2. Configuration 2: PostgreSQL + SendGrid + File Logger")
    postgres_db = PostgreSQLDatabase()
    sendgrid_email = SendGridEmailService()
    file_logger = FileLogger("app.log")
    
    user_service2 = UserService(postgres_db, sendgrid_email, file_logger)
    user_service2.register_user({"name": "Bob", "email": "bob@example.com"})
    
    print("\n" + "="*50)
    
    # Configuration 3: MongoDB + SMTP + Console Logger
    print("\n3. Configuration 3: MongoDB + SMTP + Console Logger")
    mongo_db = MongoDatabase()
    user_service3 = UserService(mongo_db, smtp_email, console_logger)
    user_service3.register_user({"name": "Charlie", "email": "charlie@example.com"})
    
    print("\n" + "="*50)
    
    # Using Dependency Injection Container
    print("\n4. Using Dependency Injection Container:")
    container = DIContainer()
    
    # Register services
    container.register_instance(DatabaseInterface, MySQLDatabase())
    container.register_instance(EmailServiceInterface, SMTPEmailService())
    container.register_instance(LoggerInterface, ConsoleLogger())
    
    # Resolve dependencies
    db = container.resolve(DatabaseInterface)
    email = container.resolve(EmailServiceInterface)
    logger = container.resolve(LoggerInterface)
    
    user_service_di = UserService(db, email, logger)
    user_service_di.register_user({"name": "Diana", "email": "diana@example.com"})
    
    print("\n5. DIP Benefits:")
    print("- High-level modules don't depend on low-level modules")
    print("- Easy to switch implementations (database, email service, logger)")
    print("- Highly testable with mock implementations")
    print("- Flexible and maintainable architecture")
    print("- Follows Hollywood Principle: 'Don't call us, we'll call you'")
    
    # Show users from different databases
    print("\n6. Retrieved Users from Different Databases:")
    print("MySQL users:", user_service1.get_all_users())
    print("PostgreSQL users:", user_service2.get_all_users())
    print("MongoDB users:", user_service3.get_all_users())


if __name__ == "__main__":
    demonstrate_dip()
