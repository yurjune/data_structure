class Queue:
    def __init__(self):
        self.queue = []

    def sizes(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return  # return None
        dequeue_item = self.queue[0]
        self.queue = self.queue[1:]
        return dequeue_item

    def peek(self):
        if self.is_empty():
            print("Queue is Empty")
            return  # return None
        return self.queue[-1]

a = Queue()

a.enqueue("hello")
a.enqueue("hi")
a.enqueue("bye")
a.enqueue("farewell")

print('peek: ', end='')
print(a.peek())

print('차례로 꺼내기:')
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())