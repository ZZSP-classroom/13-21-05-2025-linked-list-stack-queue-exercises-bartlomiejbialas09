class Stack:
    def __init__(self):
        self.stack = []

    def push(self, action):
        self.stack.append(action)

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            raise IndexError("peek from empty stack")
        return self.stack[-1]

if __name__ == "__main__":
    editor_stack = Stack()

    editor_stack.push("Typed: Hello")
    editor_stack.push("Typed: World")
    editor_stack.push("Deleted: World")

    print("Undoing:", editor_stack.pop())
    print("Undoing:", editor_stack.pop())
    print("Next action:", editor_stack.peek())