"""
Interface Segregation Principle (ISP) Examples
"""
from abc import ABC, abstractmethod


# BAD EXAMPLE: Fat interface that violates ISP
class BadWorker(ABC):
    """Fat interface that forces clients to depend on methods they don't use"""
    
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass
    
    @abstractmethod
    def take_break(self):
        pass


class BadHumanWorker(BadWorker):
    """Human worker can implement all methods"""
    
    def work(self):
        return "Human is working"
    
    def eat(self):
        return "Human is eating"
    
    def sleep(self):
        return "Human is sleeping"
    
    def take_break(self):
        return "Human is taking a break"


class BadRobotWorker(BadWorker):
    """Robot worker is forced to implement methods it doesn't need"""
    
    def work(self):
        return "Robot is working"
    
    def eat(self):
        # Robots don't eat - forced to implement unused method
        raise NotImplementedError("Robots don't eat")
    
    def sleep(self):
        # Robots don't sleep - forced to implement unused method
        raise NotImplementedError("Robots don't sleep")
    
    def take_break(self):
        # Robots don't take breaks - forced to implement unused method
        raise NotImplementedError("Robots don't take breaks")


# GOOD EXAMPLE: Segregated interfaces following ISP
class Workable(ABC):
    """Interface for entities that can work"""
    
    @abstractmethod
    def work(self) -> str:
        pass


class Eatable(ABC):
    """Interface for entities that can eat"""
    
    @abstractmethod
    def eat(self) -> str:
        pass


class Sleepable(ABC):
    """Interface for entities that can sleep"""
    
    @abstractmethod
    def sleep(self) -> str:
        pass


class Breakable(ABC):
    """Interface for entities that can take breaks"""
    
    @abstractmethod
    def take_break(self) -> str:
        pass


class Rechargeable(ABC):
    """Interface for entities that can be recharged"""
    
    @abstractmethod
    def recharge(self) -> str:
        pass


class Maintainable(ABC):
    """Interface for entities that can be maintained"""
    
    @abstractmethod
    def maintain(self) -> str:
        pass


# Implementations using segregated interfaces
class HumanWorker(Workable, Eatable, Sleepable, Breakable):
    """Human worker implements only relevant interfaces"""
    
    def __init__(self, name: str):
        self.name = name
    
    def work(self) -> str:
        return f"{self.name} is working productively"
    
    def eat(self) -> str:
        return f"{self.name} is eating lunch"
    
    def sleep(self) -> str:
        return f"{self.name} is sleeping peacefully"
    
    def take_break(self) -> str:
        return f"{self.name} is taking a well-deserved break"


class RobotWorker(Workable, Rechargeable, Maintainable):
    """Robot worker implements only relevant interfaces"""
    
    def __init__(self, model: str):
        self.model = model
    
    def work(self) -> str:
        return f"Robot {self.model} is working efficiently"
    
    def recharge(self) -> str:
        return f"Robot {self.model} is recharging batteries"
    
    def maintain(self) -> str:
        return f"Robot {self.model} is undergoing maintenance"


class SuperHuman(Workable, Eatable, Sleepable, Breakable, Maintainable):
    """Super human with enhanced capabilities"""
    
    def __init__(self, name: str):
        self.name = name
    
    def work(self) -> str:
        return f"SuperHuman {self.name} is working at superhuman speed"
    
    def eat(self) -> str:
        return f"SuperHuman {self.name} is eating energy bars"
    
    def sleep(self) -> str:
        return f"SuperHuman {self.name} is power-napping"
    
    def take_break(self) -> str:
        return f"SuperHuman {self.name} is meditating"
    
    def maintain(self) -> str:
        return f"SuperHuman {self.name} is doing self-maintenance"


# Client classes that depend on specific interfaces
class WorkManager:
    """Manages work-related activities - depends only on Workable"""
    
    def manage_work(self, worker: Workable) -> str:
        return f"Managing: {worker.work()}"
    
    def coordinate_work(self, workers: list[Workable]) -> str:
        results = []
        for worker in workers:
            results.append(worker.work())
        return "Coordinating work:\n" + "\n".join(f"- {result}" for result in results)


class RestaurantManager:
    """Manages meal times - depends only on Eatable"""
    
    def serve_meal(self, eater: Eatable) -> str:
        return f"Serving meal: {eater.eat()}"
    
    def organize_lunch(self, eaters: list[Eatable]) -> str:
        results = []
        for eater in eaters:
            results.append(eater.eat())
        return "Organizing lunch:\n" + "\n".join(f"- {result}" for result in results)


class MaintenanceManager:
    """Manages maintenance - depends only on Maintainable"""
    
    def schedule_maintenance(self, maintainable: Maintainable) -> str:
        return f"Scheduling: {maintainable.maintain()}"


class PowerManager:
    """Manages power/charging - depends only on Rechargeable"""
    
    def manage_power(self, rechargeable: Rechargeable) -> str:
        return f"Power management: {rechargeable.recharge()}"


# Another ISP example: Document processing
class Readable(ABC):
    """Interface for readable documents"""
    
    @abstractmethod
    def read(self) -> str:
        pass


class Writable(ABC):
    """Interface for writable documents"""
    
    @abstractmethod
    def write(self, content: str) -> str:
        pass


class Printable(ABC):
    """Interface for printable documents"""
    
    @abstractmethod
    def print_document(self) -> str:
        pass


class Scannable(ABC):
    """Interface for scannable documents"""
    
    @abstractmethod
    def scan(self) -> str:
        pass


class ReadOnlyDocument(Readable):
    """Document that can only be read"""
    
    def __init__(self, title: str):
        self.title = title
    
    def read(self) -> str:
        return f"Reading {self.title}"


class EditableDocument(Readable, Writable):
    """Document that can be read and written"""
    
    def __init__(self, title: str):
        self.title = title
    
    def read(self) -> str:
        return f"Reading {self.title}"
    
    def write(self, content: str) -> str:
        return f"Writing '{content}' to {self.title}"


class PrinterDocument(Readable, Printable):
    """Document that can be read and printed"""
    
    def __init__(self, title: str):
        self.title = title
    
    def read(self) -> str:
        return f"Reading {self.title}"
    
    def print_document(self) -> str:
        return f"Printing {self.title}"


class MultiFunctionDocument(Readable, Writable, Printable, Scannable):
    """Document with all capabilities"""
    
    def __init__(self, title: str):
        self.title = title
    
    def read(self) -> str:
        return f"Reading {self.title}"
    
    def write(self, content: str) -> str:
        return f"Writing '{content}' to {self.title}"
    
    def print_document(self) -> str:
        return f"Printing {self.title}"
    
    def scan(self) -> str:
        return f"Scanning {self.title}"


def demonstrate_isp():
    """Demonstrate Interface Segregation Principle"""
    print("=== Interface Segregation Principle Demo ===\n")
    
    # Workers example
    print("1. Worker Management (ISP Compliant):")
    
    human = HumanWorker("Alice")
    robot = RobotWorker("R2D2")
    superhuman = SuperHuman("Superman")
    
    # Work manager only depends on Workable interface
    work_manager = WorkManager()
    workers = [human, robot, superhuman]
    print(work_manager.coordinate_work(workers))
    
    # Restaurant manager only depends on Eatable interface
    print("\n2. Restaurant Management:")
    restaurant_manager = RestaurantManager()
    eaters = [human, superhuman]  # Robot can't eat
    print(restaurant_manager.organize_lunch(eaters))
    
    # Maintenance manager only depends on Maintainable interface
    print("\n3. Maintenance Management:")
    maintenance_manager = MaintenanceManager()
    maintainables = [robot, superhuman]  # Human doesn't need maintenance
    for maintainable in maintainables:
        print(f"- {maintenance_manager.schedule_maintenance(maintainable)}")
    
    # Power manager only depends on Rechargeable interface
    print("\n4. Power Management:")
    power_manager = PowerManager()
    print(f"- {power_manager.manage_power(robot)}")  # Only robot is rechargeable
    
    # Document processing example
    print("\n5. Document Processing (ISP Compliant):")
    
    readonly_doc = ReadOnlyDocument("Manual.pdf")
    editable_doc = EditableDocument("Report.docx")
    printer_doc = PrinterDocument("Invoice.pdf")
    multifunction_doc = MultiFunctionDocument("Presentation.pptx")
    
    # Clients depend only on interfaces they need
    print("Reading documents:")
    readable_docs = [readonly_doc, editable_doc, printer_doc, multifunction_doc]
    for doc in readable_docs:
        print(f"- {doc.read()}")
    
    print("\nPrintable documents:")
    printable_docs = [printer_doc, multifunction_doc]
    for doc in printable_docs:
        print(f"- {doc.print_document()}")
    
    print("\n6. ISP Benefits:")
    print("- Clients depend only on interfaces they actually use")
    print("- Changes to unused methods don't affect clients")
    print("- More flexible and maintainable code")
    print("- Easier testing with focused interfaces")
    print("- Better separation of concerns")


if __name__ == "__main__":
    demonstrate_isp()
