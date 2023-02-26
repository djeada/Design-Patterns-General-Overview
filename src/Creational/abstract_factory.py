"""
Applicability:

* Creating families of related or dependent objects without specifying their concrete classes.
* A system must be configured with one of multiple families of products.
* A system needs to avoid coupling to concrete classes.
* A system needs to provide a class library of products, revealing only their interfaces and not their implementations.

Consequences:

* Promotes consistency among products
* Provides a client with a simple way of creating objects
* The code is isolated from the client and thus easy to change.
* Clients might have to subclass the factories to create their own set of objects.
"""

class GUIFactory:
  def create_button(self):
    pass

  def create_text_edit(self):
      pass

class MacOSGUIFactory(GUIFactory):
  def create_button(self):
    return MacOSButton()

  def create_text_edit(self):
      return MacOSTextEdit()

class WindowsGUIFactory(GUIFactory):
  def create_button(self):
    return WindowsButton()
  def create_text_edit(self):
      return WindowsTextEdit()

class Button:
  def paint(self):
    pass

class MacOSButton(Button):
  def paint(self):
    return "MacOSButton"
class WindowsButton(Button):
  def paint(self):
    return "WindowsButton"

class TextEdit:
  def edit(self):
    pass

class MacOSTextEdit(TextEdit):
  def edit(self):
    return "MacOSTextEdit"

class WindowsTextEdit(TextEdit):
  def edit(self):
    return "WindowsTextEdit"

if __name__ == "__main__":
  os = input("Enter 'mac' for MacOS or 'win' for Windows: ")
  if os == 'mac':
    gui_factory = MacOSGUIFactory()
  elif os == 'win':
    gui_factory = WindowsGUIFactory()
  else:
    raise ValueError("Unsupported OS type")
  button = gui_factory.create_button()
  text_edit = gui_factory.create_text_edit()


print(button.paint())
print(text_edit.edit())
