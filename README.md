# DesignPatterns

A comprehensive collection of the most popular design patterns and their implementations, designed to help you understand and apply these essential patterns in your software development projects. This repository covers a wide range of design patterns, providing clear explanations, practical examples, and code implementations in various programming languages.

## Creational Patterns

Creational patterns automate object creation within code, so that functions or methods can run the code required to create new objects on your behalf. This way, you only need to explicitly adjust object creation when necessary and can rely on default behaviors otherwise.

<table>
    <thead>
        <tr>
            <th>Pattern</th>
            <th>Description</th>
            <th>Implementation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Factory Method</td>
            <td>Defines an interface for creating an object, but allows subclasses to decide which class to instantiate based on the input parameters. This pattern is useful when you want to decouple the code that creates the object from the code that uses the object.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Abstract Factory</td>
            <td>Provides an interface for creating families of related or dependent objects without specifying their concrete classes. This pattern is useful when you want to create a set of related objects that work together, but you don't want to tie your code to specific implementations.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Builder</td>
            <td>Separates the construction of a complex object from its representation so that the same construction process can create different representations. This pattern is useful when you want to create objects that have many configuration options, but you don't want to create a separate constructor for each possible combination.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Singleton</td>
            <td>Ensures that a class has only one instance and provides a global point of access to that instance. This pattern is useful when you want to restrict the number of instances of a class to one, and you want to provide a way to access that instance from anywhere in your code.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Prototype</td>
            <td>Specifies the kinds of objects to create using a prototypical instance, and creates new objects by copying this prototype. This pattern is useful when you want to create objects that are similar to existing objects, but with some modifications, and you want to avoid the overhead of creating a new object from scratch.</td>
            <td><a href="">Python</a></td>
        </tr>
    </tbody>
</table>


## Structural

Structural patterns focus on the composition of classes and objects to provide additional functionality through inheritance and interfaces. In object-oriented programming, an interface is a class or type that specifies method signatures and behaviors for other classes that implement it.

<table>
    <thead>
        <tr>
            <th>Pattern</th>
            <th>Description</th>
            <th>Implementation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Adapter</td>
            <td>Convert the interface of a class into another interface that clients expect. This pattern allows classes with incompatible interfaces to work together by wrapping its own interface around that of an existing class.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Facade</td>
            <td>Provide a simplified interface to a set of interfaces in a subsystem. This pattern defines a higher-level interface that makes the subsystem easier to use by hiding its complexity.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Proxy</td>
            <td>Provide a surrogate or placeholder for another object to control access to it. This pattern creates a representative object that controls access to another object, which may be remote, expensive to create, or require a protected access.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Decorator</td>
            <td>Add responsibilities to an object dynamically, without changing its underlying structure. This pattern allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Bridge</td>
            <td>Decouple an abstraction from its implementation, allowing the two to vary independently. This pattern involves an interface or abstract class that acts as a bridge between the abstraction and the implementation, enabling them to work together without being dependent on each other.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Composite</td>
            <td>Compose objects into tree structures to represent part-whole hierarchies. This pattern lets clients treat individual objects and compositions of objects uniformly by defining a common interface for both.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Flyweight</td>
            <td>Use sharing to support large numbers of objects efficiently. This pattern allows objects to share common state and minimize memory usage by recognizing that some parts of an object's state can be shared between multiple instances.</td>
            <td><a href="">Python</a></td>
        </tr>
    </tbody>
</table> 

## Behavioral

Behavioral patterns deal with communication and object interaction, including how objects are assigned and work together to achieve certain behaviors.

<table>
    <thead>
        <tr>
            <th>Pattern</th>
            <th>Description</th>
            <th>Implementation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Strategy</td>
            <td>Defines a family of algorithms, encapsulates each one, and makes them interchangeable. With composition over inheritance, the Strategy pattern allows clients to vary the algorithm independently from the client. This pattern makes it easy to add or modify algorithms without changing the existing code.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Observer</td>
            <td>Defines a one-to-many dependency between objects, such that when one object changes state, all its dependents are notified and updated automatically. The Observer pattern decouples the subject from the observers, allowing multiple observers to subscribe to a single subject. This pattern can be used for event handling, where events are generated and processed by different objects.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Command</td>
            <td>Encapsulates a request as an object, allowing clients to parameterize different requests, queue or log requests, and support undoable operations. The Command pattern decouples the object that invokes the operation from the object that knows how to perform it, making it easy to add new commands without changing the existing code.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Iterator</td>
            <td>Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation. The Iterator pattern decouples the client from the collection object, allowing the collection to change its internal representation without affecting the client's code. This pattern is used to provide a standard way of accessing elements of a collection, regardless of its implementation.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Null object</td>
            <td>Provides a default object that implements a null or neutral behavior, allowing the client to avoid using null references. The Null Object pattern eliminates the need for explicit null checks, making the code more readable and less prone to errors.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>State</td>
            <td>Allows an object's behavior to change when its internal state changes. The State pattern encapsulates each state as an object, and delegates the behavior to the state object. This pattern decouples the behavior from the context, allowing the behavior to vary independently of the context. This pattern is used to manage the state of an object, and to define different behaviors for different states.</td>
            <td><a href="">Python</a></td>
        </tr>
        <tr>
            <td>Visitor</td>
            <td>Represents an operation to be performed on the elements of an object structure. The Visitor pattern decouples the algorithm from the objects on which it operates, allowing the algorithm to be changed without affecting the objects. This pattern is used when we have a complex object structure with many types of objects, and we want to define a new operation on the objects without changing their classes.</td>
            <td><a href="">Python</a></td>
        </tr>
    </tbody>
</table>

## Refrences

* https://pl.cs.jhu.edu/oose/lectures/design-patterns.shtml
* https://martinfowler.com/
* http://cleancoder.com/
* https://github.com/skimedic/presentations/tree/main/Patterns/Current
* https://en.wikipedia.org/wiki/List_of_software_architecture_styles_and_patterns
* https://python-patterns.guide/

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
