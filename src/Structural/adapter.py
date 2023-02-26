"""
In this example, we have a EuropeanSocketInterface which defines the methods for a European socket. We also have a Socket class which implements the EuropeanSocketInterface. The USASocketInterface is a target interface that specifies the methods required for a US socket.

The Adapter class adapts the Socket class to the USASocketInterface. It has an instance of the Socket class and implements the USASocketInterface. The voltage method is changed to return 110, the live method returns the live value from the Socket class, and the neutral method returns the neutral value from the Socket class.

Finally, we have the ElectricKettle class which is a client of the USASocketInterface. It takes an instance of the USASocketInterface and boils water using the power from the socket. If the voltage is greater than 110, it prints "Kettle is on fire!" Otherwise, if the live value is 1 and the neutral value is -1, it prints "Coffee time!" Otherwise, it prints "No power."

In the usage section, we create an instance of the Socket class, an instance of the Adapter class, and an instance of the ElectricKettle class. We pass the instance of the Adapter class to the ElectricKettle class and call the boil method. The Adapter class adapts the Socket class to the USASocketInterface, so the ElectricKettle class is able to use the power from the European socket through the adapter.
"""

# Adaptee interface
class EuropeanSocketInterface:
    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass

    def earth(self):
        pass


# Adaptee
class Socket(EuropeanSocketInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


# Target interface
class USASocketInterface:
    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass


# Adapter
class Adapter(USASocketInterface):
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.socket.live()

    def neutral(self):
        return self.socket.neutral()


# Client
class ElectricKettle:
    def __init__(self, socket):
        self.socket = socket

    def boil(self):
        if self.socket.voltage() > 110:
            print("Kettle is on fire!")
        else:
            if self.socket.live() == 1 and self.socket.neutral() == -1:
                print("Coffee time!")
            else:
                print("No power.")


# Usage
socket = Socket()
adapter = Adapter(socket)
kettle = ElectricKettle(adapter)
kettle.boil()
