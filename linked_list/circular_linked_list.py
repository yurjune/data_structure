class CList:

    class _Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.last = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    # 항상 last의 다음 위치(맨 앞자리)에만 추가 가능
    def insert(self, item):
        n = self._Node(item, None)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
        self.size += 1

    def first(self):
        if self.is_empty():
            raise EmptyError('underflow')
        f = self.last.next
        return f.item

    def delete(self):
        if self.is_empty():
            raise EmptyError("underflow")
        if self.size == 1:
            self.last = None
        else:
            x = self.last.next
            self.last.next = x.next
        self.size -= 1

    def print_list(self):
        if self.is_empty():
            print("리스트 비어있음")
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item, '=> ', end='')
                p = p.next
            print(p.item)


class EmptyError(Exception):
    pass


s = CList()
s.insert('pear')
s.insert('cherry')
s.insert('orange')
s.insert('apple')
s.print_list()
print('s의 길이:', s.size)
print('s의 첫 항목:', s.first())

s.delete()
print('첫 노드 삭제 후: ', end='')
s.print_list()
print('s의 길이:', s.size)
print('s의 첫 항목:', s.first())

s.delete()
print('첫 노드 삭제 후: ', end='')
s.print_list()
s.delete()
print('첫 노드 삭제 후: ', end='')
s.print_list()
s.delete()
print('첫 노드 삭제 후: ', end='')
s.print_list()
