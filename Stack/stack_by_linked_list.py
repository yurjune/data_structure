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
            new_top = self.top
            print('(top) ', end='')
            while new_top.under:
                print(new_top.item, '> ', end='')
                new_top = new_top.under
            print(new_top.item, "(bottom)")


stack = LinkedListStack()

stack.push('apple')
stack.push('banana')
stack.push('kiwi')
stack.push('mango')
stack.push('cake')
stack.print_stack()

print(stack.pop())
print(stack.pop())
stack.print_stack()

print(stack.peek())

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print("다 꺼낸후:\t", end='')
stack.print_stack()
