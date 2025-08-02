# Flyweight Pattern

## Intent
Use sharing to support large numbers of fine-grained objects efficiently.

## Structure
- Flyweight: declares an interface through which flyweights can receive and act on extrinsic state
- ConcreteFlyweight: implements the Flyweight interface and adds storage for intrinsic state
- UnsharedConcreteFlyweight: not all Flyweight subclasses need to be shared
- FlyweightFactory: creates and manages flyweight objects
- Context: maintains a reference to flyweight(s) and stores extrinsic state

## When to Use
- An application uses a large number of objects
- Storage costs are high because of the sheer quantity of objects
- Most object state can be made extrinsic
- Groups of objects may be replaced by relatively few shared objects once extrinsic state is removed

## Example Use Cases
- Text editors (character objects with formatting)
- Game development (particles, bullets, terrain tiles)
- Web browsers (DOM nodes, style objects)
- Graphics systems (geometric shapes)
- Caching systems

## Implementation Considerations
- Intrinsic vs. extrinsic state separation
- Managing extrinsic state
- Client responsibilities
- Thread safety in flyweight factories
- Memory vs. computation trade-offs
