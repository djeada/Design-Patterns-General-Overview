The Command Pattern is a behavioral pattern that enables an object to encapsulate all information needed to execute an action or trigger an event at a later time. The main idea is to separate the object that invokes an operation from the one that actually performs it.

Applicability:

    Parameterize objects by an action to perform
    Specify, queue and execute requests at different times
    Support undo
    Support logging changes that can be reapplied after a crash
    Structure a system around high-level operations built out of primitives

Consequences:

    Decouples the object that invokes the operation from the one that performs it
    Since commands are objects they can be explicitly manipulated
    Can group commands into composite commands
    Easy to add new commands without changing existing code

Here's an example:

Suppose we have a simple text editor that allows users to type in some text, and perform basic text editing operations like copy, paste, and cut. We can use the Command Pattern to implement these operations as separate objects.

To do this, we create an abstract Command class that defines an interface for executing commands. We also create several concrete Command classes, each representing a specific text editing operation (e.g. CopyCommand, PasteCommand, CutCommand). Each concrete Command class implements the execute method defined by the Command interface, which encapsulates the code for performing the corresponding text editing operation.

We then create a separate Invoker class that takes a Command object as input and executes it when requested. This decouples the object that invokes the command from the one that performs it.

Finally, we can create a Client class that instantiates the Invoker object and sets its Command object to one of the concrete Command objects. This allows the user to select which text editing operation to perform, and triggers the corresponding Command object to execute its code.
