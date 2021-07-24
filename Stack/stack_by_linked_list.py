# 스택: 후입선출(LIFO)
# 큐: 선입선출(FIFO)
# 직접 구현: 부정확할 수 있음
# 단일연결리스트로 구현한 스택
# 추가된 노드는 새로운 top이 되고, 이전 top을 under로 가리킨다
# top부터 꺼낸다

class Node:
    def __init__(self, item, link):
        self.item = item
        self.under = link


class LinkedListStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        new_node = Node(item, self.top)
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.size != 0:
            target = self.top
            self.top = target.under
            self.size -= 1
            return target.item

    def peek(self):
        if self.size != 0:  # self.size == 0 이면 자동으로 None
            return self.top.item

    def print_stack(self):
        if self.size != 0:
            curr = self.top
            print('(top) ', end='')
            while curr.under:
                print(curr.item, '> ', end='')
                curr = curr.under
            print(curr.item, "(bottom)")


stack = LinkedListStack()

stack.push('apricot')
stack.push('grape')
stack.push('kiwi')
stack.push('mango')
stack.push('cake')
stack.print_stack()

print("peek: ", end='')
print(stack.peek())

print("차례로 꺼내기:")
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.print_stack()
