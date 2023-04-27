class CList:

    class Node:
        def __init__(self, item, next):
            self.item = item
            self.next = next

    def __init__(self):
        self.last = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    # last의 다음 위치(맨 앞자리)에만 추가 가능
    def insert(self, item):
        new_node = self.Node(item, None)
        if self.is_empty():
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node   # 순환
        self.size += 1

    def first_item(self):
        if self.is_empty():
            raise EmptyError('underflow')
        first = self.last.next
        return first.item

    def last_item(self):
        if self.is_empty():
            raise EmptyError('underflow')
        return self.last.item

    def delete(self):   # 맨 앞 노드 삭제
        if self.is_empty():
            raise EmptyError("underflow")
        if self.size == 1:
            self.last = None
        else:
            first = self.last.next
            self.last.next = first.next
        self.size -= 1

    def print_list(self):
        if self.is_empty():
            return print('비어 있음')
        first = self.last.next
        curr = first
        while curr.next != first:
            print(curr.item, '-> ', end='')
            curr = curr.next
        print(curr.item)


class EmptyError(Exception):
    pass


clist = CList()
clist.insert('grape')
clist.insert('grapefruit')
clist.insert('plum')
clist.insert('lemon')
clist.print_list()
print(f'first: {clist.first_item()}, last: {clist.last_item()}')

clist.delete()
clist.print_list()

