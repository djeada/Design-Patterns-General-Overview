# Prototype Pattern

## Intent
Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

## Structure
- Prototype: declares an interface for cloning itself
- ConcretePrototype: implements an operation for cloning itself
- Client: creates a new object by asking a prototype to clone itself

## When to Use
- When the classes to instantiate are specified at runtime
- To avoid building a class hierarchy of factories that parallels the class hierarchy of products
- When instances of a class can have one of only a few different combinations of state

## Example Use Cases
- Object creation is expensive (database queries, network calls)
- Creating objects with complex initialization
- Game development (cloning game entities)
- GUI component templates
- Configuration object templates

## Implementation Considerations
- Deep vs. shallow copying
- Clone method implementation
- Prototype manager/registry
- Serialization-based cloning
- Copy constructors vs. clone methods
