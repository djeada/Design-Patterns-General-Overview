"""
Applicability
- When a system has a complex structure made up of many classes, and you need to perform operations that depend on those classes.
- When the set of classes is stable, but you need to define new operations that can be applied to them.
- When it is desirable to group related behavior in a single class.
- When it is necessary to add new operations to a class hierarchy frequently, without modifying the classes themselves.

Consequences
- It is easy to add new operations to the system by defining new Visitor classes.
- Related behavior can be grouped together in a single Visitor class.
- The Visitor pattern separates the algorithms from the object structure.
- Adding new classes to the object structure can be difficult because you need to update all the Visitor classes.
- The Visitor pattern requires that the objects being visited expose an interface that can be used by the Visitor.
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def accept(self, visitor):
        visitor.visit_employee(self)


class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def accept(self, visitor):
        visitor.visit_department(self)

    def get_total_salary(self):
        return sum(e.salary for e in self.employees)


class PayrollVisitor:
    def __init__(self):
        self.total_salary = 0

    def visit_employee(self, employee):
        self.total_salary += employee.salary

    def visit_department(self, department):
        self.total_salary += department.get_total_salary()


# Example usage
employees = [Employee("Alice", 50000), Employee("Bob", 60000)]
dept = Department("Engineering", employees)
payroll = PayrollVisitor()
dept.accept(payroll)
print(f"Total salary: {payroll.total_salary}")
