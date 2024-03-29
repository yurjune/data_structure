# 단일연결리스트로 구현한 큐
# 추가된 노드는 새 rear가 되고, 이전 rear는 새 rear를 next로 가리킨다
# front부터 꺼낸다

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, item):
        new_node = Node(item, None)
        if self.size == 0:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = self.rear.next
        self.size += 1
        # self.rear.next를 바꾸면 self.front.next도 바뀐다

    def dequeue(self):
        if self.size == 0:
            return None
        target_item = self.front.item
        self.front = self.front.next
        self.size -= 1
        return target_item

    def peek(self):
        target = self.front
        for i in range(self.size - 1):
            target = target.next
        return target.item

    def print_queue(self):
        if self.size == 0:
            return None
        curr = self.front
        print('(front) ', end='')
        while curr.next:
            print(curr.item, '=> ', end='')
            curr = curr.next
        print(curr.item, '(rear)')


queue = LinkedListQueue()
queue.enqueue("apricot")
queue.enqueue("peach")
queue.enqueue("grape")
queue.enqueue("muscat")
queue.print_queue()

print('peek: ', end='')
print(queue.peek())
print('차례로 꺼내기:')
print(queue.dequeue())
print(queue.dequeue())
queue.print_queue()
