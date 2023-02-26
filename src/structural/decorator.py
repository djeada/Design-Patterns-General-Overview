"""
n this example, TextEditor is the base component that has a write method. TextDecorator is an abstract base class for all decorators, and BoldDecorator and ItalicDecorator are concrete decorator classes. Each decorator class overrides the write method and adds its own formatting to the text before calling the write method of the base component.

In the main program, we first create an instance of the TextEditor and call its write method to write some text to the console. Then, we create a BoldDecorator and an ItalicDecorator, and use them to decorate the original TextEditor. Finally, we create a BoldDecorator that decorates an ItalicDecorator that decorates the original TextEditor, resulting in text that is both bold and italicized.
"""


class TextEditor:
    """
    Basic text editor with a write method.
    """

    def write(self, text):
        print(f"Writing: {text}")


class TextDecorator:
    """
    Base class for text decorators.
    """

    def __init__(self, editor):
        self.editor = editor

    def write(self, text):
        self.editor.write(text)


class BoldDecorator(TextDecorator):
    """
    Decorator that adds bold formatting to text.
    """

    def write(self, text):
        self.editor.write(f"<b>{text}</b>")


class ItalicDecorator(TextDecorator):
    """
    Decorator that adds italic formatting to text.
    """

    def write(self, text):
        self.editor.write(f"<i>{text}</i>")


if __name__ == "__main__":
    editor = TextEditor()
    editor.write("Hello, world!")

    bold_editor = BoldDecorator(editor)
    bold_editor.write("Hello, world!")

    italic_editor = ItalicDecorator(editor)
    italic_editor.write("Hello, world!")

    bold_italic_editor = BoldDecorator(ItalicDecorator(editor))
    bold_italic_editor.write("Hello, world!")
