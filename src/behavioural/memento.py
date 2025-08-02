"""
Memento Pattern Implementation
"""
from typing import List
from datetime import datetime


class Memento:
    """Memento storing the state of an originator."""
    
    def __init__(self, state: str):
        self._state = state
        self._date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def get_state(self) -> str:
        """Get the stored state."""
        return self._state
    
    def get_name(self) -> str:
        """Get the memento name with timestamp."""
        return f"{self._date} / ({self._state[:9]}...)"
    
    def get_date(self) -> str:
        """Get the creation date."""
        return self._date


class Originator:
    """Originator whose state can be saved and restored."""
    
    def __init__(self, state: str):
        self._state = state
        print(f"Originator: My initial state is: {self._state}")
    
    def do_something(self) -> None:
        """Perform some operation that changes state."""
        print("Originator: I'm doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to: {self._state}")
    
    def _generate_random_string(self, length: int = 10) -> str:
        """Generate a random string to simulate state change."""
        import string
        import random
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    def save(self) -> Memento:
        """Create a memento with current state."""
        return Memento(self._state)
    
    def restore(self, memento: Memento) -> None:
        """Restore state from memento."""
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Caretaker:
    """Caretaker managing mementos."""
    
    def __init__(self, originator: Originator):
        self._mementos: List[Memento] = []
        self._originator = originator
    
    def backup(self) -> None:
        """Create a backup of the current state."""
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())
    
    def undo(self) -> None:
        """Restore the last saved state."""
        if not self._mementos:
            print("Caretaker: No mementos to restore!")
            return
        
        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()
    
    def show_history(self) -> None:
        """Show the history of saved states."""
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)
    
    caretaker.backup()
    originator.do_something()
    
    caretaker.backup()
    originator.do_something()
    
    caretaker.backup()
    originator.do_something()
    
    print("\n")
    caretaker.show_history()
    
    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()
    
    print("\nClient: Once more!\n")
    caretaker.undo()
