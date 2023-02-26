"""
In this example, we have a Computer class that serves as a facade to the complex subsystems of CPU, Memory, and HardDrive. The Computer class encapsulates the logic of starting up the computer, and delegates the actual work to the appropriate subsystems.

The CPU, Memory, and HardDrive classes are all complex and have their own internal workings, but the Computer class provides a simplified interface to start up the computer.
"""


class CPU:
    def freeze(self):
        print("CPU: Freezing system")

    def jump(self, position):
        print(f"CPU: Jumping to memory location {position}")

    def execute(self):
        print("CPU: Executing program instructions")


class Memory:
    def load(self, position, data):
        print(f"Memory: Loading data '{data}' into memory location {position}")


class HardDrive:
    def read(self, lba, size):
        print(f"Hard Drive: Reading {size} bytes from LBA {lba}")


class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        self.cpu.freeze()
        self.memory.load(0, "BOOTLOADER")
        self.cpu.jump(0)
        self.cpu.execute()
        self.memory.load(0x400, "OS")
        self.cpu.jump(0x400)
        self.cpu.execute()
        self.hard_drive.read(0x600, 512)


if __name__ == "__main__":
    computer = Computer()
    computer.start_computer()
