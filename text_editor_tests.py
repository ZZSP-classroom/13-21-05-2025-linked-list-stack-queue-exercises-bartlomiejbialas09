import unittest
from text_editor_2 import Stack


class TestTextEditorUndo(unittest.TestCase):

    def test_push_pop(self):
        stack = Stack()
        
        stack.push("Typed: Hello")
        stack.push("Typed: World")

        self.assertEqual(stack.pop(), "Typed: World")
        self.assertEqual(stack.pop(), "Typed: Hello")
        self.assertRaises(IndexError, stack.pop)

    def test_peek(self):
        stack = Stack()

        stack.push("Typed: Hello")
        self.assertEqual(stack.peek(), "Typed: Hello")
        stack.pop()
        self.assertRaises(IndexError, stack.peek)


if __name__ == "__main__":
    unittest.main()