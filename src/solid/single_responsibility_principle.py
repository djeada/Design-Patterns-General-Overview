"""
Single Responsibility Principle (SRP) Examples
"""

# BAD EXAMPLE: Multiple responsibilities in one class
class BadUser:
    """This class violates SRP by having multiple responsibilities"""
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    # User data responsibility
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    # Database responsibility - VIOLATES SRP
    def save_to_database(self):
        print(f"Saving user {self.name} to database")
        # Database logic here
    
    # Email responsibility - VIOLATES SRP  
    def send_welcome_email(self):
        print(f"Sending welcome email to {self.email}")
        # Email sending logic here
    
    # Validation responsibility - VIOLATES SRP
    def validate_email(self):
        return "@" in self.email
    
    # Reporting responsibility - VIOLATES SRP
    def generate_user_report(self):
        return f"User Report: {self.name} ({self.email})"


# GOOD EXAMPLE: Single responsibility per class
class User:
    """User class focusing only on user data"""
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def __str__(self):
        return f"User({self.name}, {self.email})"


class UserRepository:
    """Handles user persistence - Single responsibility: Database operations"""
    
    def __init__(self):
        self.users = []  # Simulate database
    
    def save(self, user: User):
        print(f"Saving user {user.get_name()} to database")
        self.users.append(user)
    
    def find_by_email(self, email: str):
        for user in self.users:
            if user.get_email() == email:
                return user
        return None
    
    def get_all_users(self):
        return self.users.copy()


class EmailService:
    """Handles email operations - Single responsibility: Email sending"""
    
    def send_welcome_email(self, user: User):
        print(f"Sending welcome email to {user.get_email()}")
        # Email sending logic here
    
    def send_password_reset(self, user: User):
        print(f"Sending password reset email to {user.get_email()}")
    
    def send_notification(self, user: User, message: str):
        print(f"Sending notification to {user.get_email()}: {message}")


class UserValidator:
    """Handles user validation - Single responsibility: Validation"""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        return "@" in email and "." in email
    
    @staticmethod
    def validate_name(name: str) -> bool:
        return len(name.strip()) > 0
    
    @staticmethod
    def validate_user(user: User) -> bool:
        return (UserValidator.validate_name(user.get_name()) and 
                UserValidator.validate_email(user.get_email()))


class UserReportGenerator:
    """Handles report generation - Single responsibility: Reporting"""
    
    def generate_user_report(self, user: User) -> str:
        return f"User Report: {user.get_name()} ({user.get_email()})"
    
    def generate_users_summary(self, users: list) -> str:
        count = len(users)
        return f"Total users: {count}"
    
    def generate_detailed_report(self, users: list) -> str:
        report = "Detailed User Report\n"
        report += "=" * 20 + "\n"
        for user in users:
            report += f"- {user.get_name()}: {user.get_email()}\n"
        return report


class UserService:
    """Orchestrates user operations using other services"""
    
    def __init__(self, repository: UserRepository, email_service: EmailService, 
                 validator: UserValidator, report_generator: UserReportGenerator):
        self.repository = repository
        self.email_service = email_service
        self.validator = validator
        self.report_generator = report_generator
    
    def register_user(self, name: str, email: str) -> bool:
        user = User(name, email)
        
        if not self.validator.validate_user(user):
            print(f"Invalid user data for {name}")
            return False
        
        self.repository.save(user)
        self.email_service.send_welcome_email(user)
        print(f"User {name} registered successfully")
        return True
    
    def get_user_report(self, email: str) -> str:
        user = self.repository.find_by_email(email)
        if user:
            return self.report_generator.generate_user_report(user)
        return "User not found"


def demonstrate_srp():
    """Demonstrate Single Responsibility Principle"""
    print("=== Single Responsibility Principle Demo ===\n")
    
    # Initialize services
    repository = UserRepository()
    email_service = EmailService()
    validator = UserValidator()
    report_generator = UserReportGenerator()
    
    user_service = UserService(repository, email_service, validator, report_generator)
    
    # Register users
    print("1. Registering users:")
    user_service.register_user("John Doe", "john@example.com")
    user_service.register_user("Jane Smith", "jane@example.com")
    user_service.register_user("Invalid User", "invalid-email")  # Should fail validation
    
    print("\n2. Generating reports:")
    print(user_service.get_user_report("john@example.com"))
    
    all_users = repository.get_all_users()
    print(report_generator.generate_users_summary(all_users))
    
    print("\n3. Each class has a single responsibility:")
    print("- User: Holds user data")
    print("- UserRepository: Manages persistence")
    print("- EmailService: Handles email operations")
    print("- UserValidator: Validates user data")
    print("- UserReportGenerator: Creates reports")
    print("- UserService: Orchestrates operations")


if __name__ == "__main__":
    demonstrate_srp()
