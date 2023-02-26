"""
Observer pattern example

Applicability:
- When an abstraction has two aspects, one dependent on the other, and you want to reuse each
- When change to one object requires changing others, and you don’t know how many objects need to be changed
- When an object should be able to notify others without knowing who they are

Consequences:
- Loose coupling between subject and observer, enhancing reuse
- Support for broadcast communication
- Notification can lead to further updates, causing a cascade effect
"""

class Subject:
    """
    Represents the subject being observed.
    """
    def __init__(self):
        self.observers = []
        self.state = None

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def set_state(self, state):
        self.state = state
        self.notify()

class Observer:
    """
    Represents an observer that is interested in the state of the subject.
    """
    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print(f"Observer {id(self)} updated with state {self.subject.state}")

if __name__ == "__main__":
    # Create the subject and attach observers
    subject = Subject()
    observer1 = Observer(subject)
    observer2 = Observer(subject)

    # Set the state of the subject
    subject.set_state(42)

    # Detach observer1
    subject.detach(observer1)

    # Set the state of the subject again
    subject.set_state(69)
