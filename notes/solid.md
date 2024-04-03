### Uncle Bob's SOLID principles

The SOLID principles are a set of design principles for software development that aim to improve code quality and maintainability. The principles were introduced by Robert C. Martin (a.k.a Uncle Bob) in the early 2000s and have since become a widely adopted standard in the industry. Let's take a closer look at each principle:

1. Single Responsibility Principle (SRP)

The Single Responsibility Principle states that a class should have only one reason to change. In other words, a class should have only one responsibility. This principle helps to ensure that each class is focused on a specific task, which makes the code easier to understand, modify, and maintain.

For example, consider a class that has multiple responsibilities, such as handling user input and database operations. If this class needs to be modified to handle a change in the database schema, it could break the user input functionality, making it difficult to maintain. Instead, the class should be split into two separate classes: one for user input and another for database operations.

2. Open/Closed Principle (OCP)

The Open/Closed Principle states that a class should be open for extension but closed for modification. This principle encourages the use of inheritance and interfaces to allow new functionality to be added without modifying existing code.

For example, consider a class that calculates the total cost of an order. If a new discount type needs to be added, the class should be extended to include the new discount calculation logic, rather than modifying the existing code. This ensures that the original functionality remains unchanged and allows for easier maintenance and testing.

- Good example: strategy pattern

3. Liskov Substitution Principle (LSP)

The Liskov Substitution Principle states that a subclass should be substitutable for its base class. In other words, any code that works with the base class should also work with its subclasses without requiring any modification.

For example, consider a class hierarchy of shapes, where each subclass (circle, square, etc.) has a method for calculating its area. The Liskov Substitution Principle ensures that any code that works with the base shape class, such as a method that calculates the total area of a collection of shapes, should also work with its subclasses, without needing to modify the code.

4. Interface Segregation Principle (ISP)

The Interface Segregation Principle states that a class should not be forced to implement interfaces that it does not use. This principle encourages the use of smaller, more specific interfaces, which makes the code easier to understand and maintain.

Imagine we have an interface called Printer that contains two methods: print() and scan(). We then create two classes that implement this interface: LaserPrinter and InkjetPrinter.

The LaserPrinter class needs to implement both methods since it can both print and scan documents. However, the InkjetPrinter class can only print documents, so it doesn't need the scan() method.

If we adhere to the Interface Segregation Principle, we would create a separate interface for the scan() method, such as Scanner, and have the LaserPrinter class implement both Printer and Scanner interfaces. On the other hand, the InkjetPrinter class would only implement the Printer interface, since it doesn't have scanning functionality.

5. Dependency Inversion Principle (DIP)

The Dependency Inversion Principle states that high-level modules should not depend on low-level modules, but both should depend on abstractions. This principle encourages the use of interfaces to decouple the dependencies between classes, which makes the code more flexible and maintainable.

For example, consider a class that requires an instance of another class to perform a specific task. Instead of creating a hard-coded dependency, the class should depend on an interface that can be implemented by any class that meets the required functionality. This allows for easier testing and maintenance, as the implementation can be swapped out without affecting the rest of the code.
