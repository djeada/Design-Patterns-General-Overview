"""
Iterator Pattern Implementation
"""
from abc import ABC, abstractmethod
from typing import Any, List


class Iterator(ABC):
    """Abstract iterator interface."""
    
    @abstractmethod
    def __next__(self) -> Any:
        """Return the next element."""
        pass
    
    @abstractmethod
    def has_next(self) -> bool:
        """Check if there are more elements."""
        pass


class Aggregate(ABC):
    """Abstract aggregate interface."""
    
    @abstractmethod
    def create_iterator(self) -> Iterator:
        """Create an iterator for this aggregate."""
        pass


class ConcreteIterator(Iterator):
    """Concrete iterator implementation."""
    
    def __init__(self, collection: List[Any]):
        self._collection = collection
        self._position = 0
    
    def __next__(self) -> Any:
        """Return the next element."""
        if not self.has_next():
            raise StopIteration
        
        value = self._collection[self._position]
        self._position += 1
        return value
    
    def has_next(self) -> bool:
        """Check if there are more elements."""
        return self._position < len(self._collection)


class ReverseIterator(Iterator):
    """Iterator that traverses in reverse order."""
    
    def __init__(self, collection: List[Any]):
        self._collection = collection
        self._position = len(collection) - 1
    
    def __next__(self) -> Any:
        """Return the next element in reverse order."""
        if not self.has_next():
            raise StopIteration
        
        value = self._collection[self._position]
        self._position -= 1
        return value
    
    def has_next(self) -> bool:
        """Check if there are more elements."""
        return self._position >= 0


class WordsCollection(Aggregate):
    """Concrete aggregate storing a collection of words."""
    
    def __init__(self):
        self._items: List[str] = []
    
    def add_item(self, item: str) -> None:
        """Add an item to the collection."""
        self._items.append(item)
    
    def create_iterator(self) -> Iterator:
        """Create a forward iterator."""
        return ConcreteIterator(self._items)
    
    def create_reverse_iterator(self) -> Iterator:
        """Create a reverse iterator."""
        return ReverseIterator(self._items)
    
    def __iter__(self) -> Iterator:
        """Make the collection iterable (Python iterator protocol)."""
        return ConcreteIterator(self._items)


def client_code(collection: WordsCollection) -> None:
    """Client code using the iterator."""
    print("Straight traversal:")
    iterator = collection.create_iterator()
    while iterator.has_next():
        print(next(iterator))
    
    print("\nReverse traversal:")
    reverse_iterator = collection.create_reverse_iterator()
    while reverse_iterator.has_next():
        print(next(reverse_iterator))
    
    print("\nPython-style iteration:")
    for item in collection:
        print(item)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")
    
    client_code(collection)
