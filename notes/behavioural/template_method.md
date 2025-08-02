# Template Method Pattern

## Intent
Define the skeleton of an algorithm in the superclass but let subclasses override specific steps of the algorithm without changing its structure.

## Structure
- AbstractClass: defines abstract primitive operations that concrete subclasses define to implement steps of an algorithm
- ConcreteClass: implements the primitive operations to carry out subclass-specific steps of the algorithm

## When to Use
- You want to implement the invariant parts of an algorithm once and leave it up to subclasses to implement the behavior that can vary
- Common behavior among subclasses should be factored and localized in a common class
- You want to control subclasses extensions

## Example Use Cases
- Data processing pipelines
- Testing frameworks (setup, test, teardown)
- Web framework request handling
- Sorting algorithms with custom comparison
- File parsing with different formats

## Implementation Considerations
- Use of hooks (optional steps) vs. required abstract methods
- Minimize the number of primitive operations
- Naming conventions for template methods vs. primitive operations
- Consider using strategy pattern as an alternative
