class SList:

    class Node:
        def __init__(self, item, next):
            self.item = item
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def insert_after(self, item, node):
        node.next = self.Node(item, node.next)
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        self.head = self.head.next
        self.size -= 1

    def delete_after(self, node):
        if self.is_empty():
            raise EmptyError('Underflow')
        node.next = node.next.next
        self.size -= 1

    def search(self, target):   # 인덱스를 반환(인덱스는 0부터)
        curr = self.head
        for i in range(self.size):
            if target == curr.item:
                return i
            curr = curr.next  # 순차탐색
        return None

    def print_list(self):
        if self.is_empty():
            return print('비어 있음')
        curr = self.head
        while curr.next != None:
            print(curr.item, '-> ', end='')
            curr = curr.next
        print(curr.item)


class EmptyError(Exception):
    pass


slist = SList()
slist.insert_front('mango')
slist.insert_front('melon')
slist.insert_front('pear')
slist.insert_front('lemon')
slist.print_list()

slist.insert_after('kiwi', slist.head)
slist.insert_after('orange', slist.head)
slist.print_list()
print(f'melon은 {slist.search("melon")}번 째')

slist.delete_after(slist.head)
slist.delete_front()
slist.print_list()
