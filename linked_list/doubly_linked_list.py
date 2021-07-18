class DList:

    class Node:
        def __init__(self, item, prev, next):
            self.item = item
            self.prev = prev
            self.next = next

    def __init__(self):
        # dummy nodes: head, tail
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0   # head, tail no-count

    def is_empty(self):
        return self.size == 0

    def insert_before(self, item, node):
        new_node = self.Node(item, node.prev, node)
        node.prev.next = new_node
        node.prev = new_node
        self.size += 1

    def insert_after(self, item, node):
        new_node = self.Node(item, node, node.next)
        node.next.prev = new_node
        node.next = new_node
        self.size += 1

    def delete(self, target):
        if self.is_empty():
            raise EmptyError('Underflow')
        target.prev.next = target.next
        target.next.prev = target.prev
        self.size -= 1

    def print_list(self):
        if self.is_empty():
            return print('비어 있음')
        curr = self.head.next
        while curr.next != self.tail:
            print(curr.item, "<=> ", end='')
            curr = curr.next
        print(curr.item)


class EmptyError(Exception):
    pass


dlist = DList()
dlist.insert_before("apple", dlist.tail)
dlist.insert_before("banana", dlist.tail)
dlist.insert_before("pineapple", dlist.tail)
dlist.print_list()

dlist.insert_after("kiwi", dlist.head)
dlist.insert_after("peach", dlist.head)
dlist.insert_after("pear", dlist.head)
dlist.print_list()

dlist.delete(dlist.head.next)
dlist.delete(dlist.tail.prev)
dlist.print_list()
