class DList:

    class Node:
        def __init__(self, item, prev, link):
            self.item = item
            self.prev = prev
            self.next = link

    def __init__(self):
        # head와 tail에 대응하는 노드 2개 생성
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0   # head, tail no-count

    def is_empty(self):
        return self.size == 0

    def insert_before(self, p, item):
        t = p.prev
        n = self.Node(item, t, p)   # t -> n -> p
        # 새 노드와 앞뒤 연결
        p.prev = n
        t.next = n
        self.size += 1

    def insert_after(self, p, item):
        t = p.next
        n = self.Node(item, p, t)   # p -> n -> t
        t.prev = n
        p.next = n
        self.size += 1

    def delete(self, x):
        if self.is_empty():
            raise EmptyError('Underflow')
        f = x.prev
        r = x.next
        f.next = r
        r.prev = f
        self.size -= 1
        return x.item

    def print_list(self):
        if self.is_empty():
            print("리스트 비어있음")
            return
        p = self.head.next  # 초기 head 건너뛰기
        while p != self.tail:   # 초기 tail 건너뛰기
            if p.next != self.tail:
                print(p.item, ' <=> ', end='')
            else:
                print(p.item)
            p = p.next


class EmptyError(Exception):
    pass


s = DList()  # 이중 연결 리스트 생성
s.insert_after(s.head, 'apple')
s.insert_before(s.tail, 'orange')
s.insert_before(s.tail, 'cherry')
s.insert_after(s.head.next, 'pear')
s.print_list()

print('마지막 노드 삭제 후:\t', end='')
s.delete(s.tail.prev)
s.print_list()

print('맨 끝에 포도 삽입 후:\t', end='')
s.insert_before(s.tail, 'grape')
s.print_list()

print('첫 노드 삭제 후:\t', end='')
s.delete(s.head.next)
s.print_list()

print('두 번째 노드 삭제 후:\t', end='')
s.delete(s.head.next.next)
s.print_list()

print('첫 노드 삭제 후:\t', end='')
s.delete(s.head.next)
s.print_list()

print('첫 노드 삭제 후:\t', end='')
s.delete(s.head.next)
s.print_list()
