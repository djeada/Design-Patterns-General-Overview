"""
Demonstration of the Strategy design pattern to solve the problems with using inheritance for different variants of a behavior in object-oriented programming.

Problem:
- When multiple classes differ only in their behavior, using inheritance can lead to code duplication and maintenance problems.
- Inheriting a behavior that is not needed in a subclass can lead to code bloat and complexity.

Solution:
- Strategy pattern separates the behavior from the classes that use it, allowing for more flexible and dynamic code.
- Instead of using inheritance, a common interface is used to define the behavior, and concrete implementations of the interface are provided for each variant.
- The context object that uses the behavior can then use any of the available concrete implementations of the behavior, without needing to know about the details of how it works.

In this example, we demonstrate the use of the Strategy pattern to implement different types of ducks that can quack and fly in different ways, without relying on inheritance. 
"""


class Duck:
    def __init__(self, quack_behavior, fly_behavior):
        self.quack_behavior = quack_behavior
        self.fly_behavior = fly_behavior

    def quack(self):
        print(self.quack_behavior.quack())

    def fly(self):
        print(self.fly_behavior.fly())


class QuackBehavior:
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        return "Quack"


class Squeak(QuackBehavior):
    def quack(self):
        return "Squeak"


class MuteQuack(QuackBehavior):
    def quack(self):
        return "<< Silence >>"


class FlyBehavior:
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        return "I'm flying!!"


class FlyNoWay(FlyBehavior):
    def fly(self):
        return "<< I can't fly >>"


if __name__ == "__main__":
    simple_duck = Duck(Quack(), FlyWithWings())
    fancy_duck = Duck(Squeak(), FlyNoWay())
    silent_duck = Duck(MuteQuack(), FlyWithWings())

    simple_duck.fly()
    simple_duck.quack()

    fancy_duck.fly()
    fancy_duck.quack()

    silent_duck.fly()
    silent_duck.quack()
