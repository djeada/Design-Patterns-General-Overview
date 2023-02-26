"""
The Mediator pattern is used when a set of objects communicate in well-defined but complex ways, and reusing an object is difficult because it communicates with others. It's also useful when a behavior distributed between several classes should be customizable without a lot of subclassing.

In this example, we have a chat room where users can send messages to each other. Instead of each user communicating directly with every other user, a Mediator class called ChatRoom is introduced to handle the communication between users. This decouples the users from each other, enhancing reuse, and simplifies the object protocols from many-to-many to one-to-many.

In this example, the ChatRoom class acts as a mediator between the User objects. Users can send messages to each other through the ChatRoom, but they do not communicate with each other directly. This decouples the users from each other, making it easier to add new users or modify the behavior of existing users without changing the code of other users. The ChatRoom class also simplifies the protocol for communication, changing it from a many-to-many relationship to a one-to-many relationship. The consequences of using the Mediator pattern include avoiding excessive subclassing to customize behavior, centralizing control, and abstracting how objects cooperate into the mediator. However, there is a danger of creating a mediator monolith if the Mediator class becomes too complex.

Consequences of using the Mediator pattern include avoiding excessive subclassing to customize behavior, centralizing control, and abstracting how objects cooperate into the mediator. However, there is a danger of creating a mediator monolith if the Mediator class becomes too complex.

"""

class ChatRoom:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, sender, message):
        for user in self.users:
            if user != sender:
                user.receive_message(sender, message)

class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, message):
        chat_room.send_message(self, message)

    def receive_message(self, sender, message):
        print(f"{self.name} received a message from {sender.name}: {message}")

chat_room = ChatRoom()

john = User("John")
jane = User("Jane")
jim = User("Jim")

chat_room.add_user(john)
chat_room.add_user(jane)
chat_room.add_user(jim)

john.send_message("Hello everyone!")
jane.send_message("Hey John, what's up?")
jim.send_message("Nothing much, just chilling.")

"""
Output:
Jane received a message from John: Hello everyone!
Jim received a message from John: Hello everyone!
John received a message from Jane: Hey John, what's up?
Jim received a message from Jane: Hey John, what's up?
John received a message from Jim: Nothing much, just chilling.
Jane received a message from Jim: Nothing much, just chilling.
"""
