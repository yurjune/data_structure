class SList:

    class Node:
        def __init__(self, item, link):  # 노드 생성자
            self.item = item  # 항목
            self.next = link  # 다음 노드 레퍼런스

    def __init__(self):  # 단순 연결 리스트 생성자
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):  # 연결 리스트의 맨 앞에 새 노드 삽입
        if self.is_empty():
            self.head = self.Node(item, None)  # head가 새 노드 참조
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def insert_after(self, item, p):  # p가 가리키는 노드 다음에 새 노드 삽입
        p.next = self.Node(item, p.next)  # 새 노드가 p 다음 노드
        self.size += 1

    def delete_front(self):  # 연결 리스트의 맨 앞 노드 삭제
        if self.is_empty():
            raise EmptyError('Underflow')
        else:
            self.head = self.head.next  # head가 둘째 노드를 참조
            self.size -= 1

    def delete_after(self, p):  # p가 가리키는 노드의 다음 노드 삭제
        if self.is_empty():
            raise EmptyError('Underflow')
        t = p.next  # t가 가리키는 노드가 삭제(무시)하려는 노드
        p.next = t.next
        self.size -= 1

    def search(self, target):  # target: 찾으려는 항목
        p = self.head
        for k in range(self.size):
            if target == p.item:
                return k
            p = p.next  # 순차탐색
        return None

    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, '-> ', end='')
            else:
                print(p.item)
            p = p.next  # 순차탐색


class EmptyError(Exception):
    pass


s = SList()
s.insert_front('orange')
s.insert_front('apple')
s.insert_after('cherry', s.head.next)
s.insert_front('pear')
s.print_list()

print('cherry는 %d번째' % s.search('cherry'))
print('kiwi는', s.search('kiwi'))

print('배 다음 노드 삭제 후:\t\t', end='')
s.delete_after(s.head)
s.print_list()

print('첫 노드 삭제 후:\t\t', end='')
s.delete_front()
s.print_list()

print('첫 노드로 망고, 딸기 삽입 후:\t', end='')
s.insert_front('mango')
s.insert_front('strawberry')
s.print_list()

print('오렌지 다음 노드 삭제 후:\t', end='')
s.delete_after(s.head.next.next)
s.print_list()

# p를 편하게 지정하는 방법?
