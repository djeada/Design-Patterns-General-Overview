
'''
Example
We will create a simple text editor that allows users to perform the following operations:
- Insert text at the current cursor position
- Delete text at the current cursor position
- Replace text at the current cursor position
- Undo the last operation
- Redo the last undone operation

We will use the Command pattern to implement these operations.

'''

class TextEditor:
    def __init__(self):
        self._text = ''
        self._cursor = 0
        self._history = []

    def insert(self, text):
        self._text = self._text[:self._cursor] + text + self._text[self._cursor:]
        self._history.append(InsertCommand(self, text))

    def delete(self, n):
        text = self._text[self._cursor:self._cursor + n]
        self._text = self._text[:self._cursor] + self._text[self._cursor + n:]
        self._history.append(DeleteCommand(self, text))

    def replace(self, n, text):
        old_text = self._text[self._cursor:self._cursor + n]
        self._text = self._text[:self._cursor] + text + self._text[self._cursor + n:]
        self._history.append(ReplaceCommand(self, old_text, text))

    def undo(self):
        if not self._history:
            return
        command = self._history.pop()
        command.undo()

    def redo(self):
        pass

class Command:
    def __init__(self, editor):
        self._editor = editor

    def execute(self):
        pass

    def undo(self):
        pass

class InsertCommand(Command):
    def __init__(self, editor, text):
        super().__init__(editor)
        self._text = text

    def execute(self):
        self._editor.insert(self._text)

    def undo(self):
        self._editor.delete(len(self._text))

class DeleteCommand(Command):
    def __init__(self, editor, text):
        super().__init__(editor)
        self._text = text

    def execute(self):
        self._editor.delete(len(self._text))

    def undo(self):
        self._editor.insert(self._text)

class ReplaceCommand(Command):
    def __init__(self, editor, old_text, new_text):
        super().__init__(editor)
        self._old_text = old_text
        self._new_text = new_text

    def execute(self):
        self._editor.replace(len(self._old_text), self._new_text)

    def undo(self):
        self._editor.replace(len(self._new_text), self._old_text)
