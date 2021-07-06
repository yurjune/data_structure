class Stack:
    def __init__(self):
        self.stack = []

    def sizes(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack.pop()  # 점검

    def peek(self):  # top항목 접근
        if self.is_empty():
            return "Stack is Empty"
        return self.stack[-1]


a = Stack()

a.push("hello")
a.push("hi")
a.push("bye")
a.push("farewell")

print(a.peek())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
