# 폐쇄주소 방식(closed addresing)
class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

class Chaning:
    def __init__(self, size):
        self.M = size
        self.slot = [None]*size
        self.data = [None]*size

    def hash(self, key):
        return key % self.M

    def put(self, key, value):
        i = self.hash(key)
        node = self.slot[i]
        while node != None:
            # 이미 키가 있다면 데이터만 갱신
            if node.key == key:
                node.value = value
                return
            node = node.next
        # 단순연결리스트 맨 앞에 삽입
        self.slot[i] = Node(key, value, self.slot[i])

    def get(self, key):
        i = self.hash(key)
        node = self.slot[i]
        while node != None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def print_table(self):
        for i in range(self.M):
            print('%2d' % i, end='')
            node = self.slot[i]
            while node:
                print(f' --> [{node.key}, {node.value}]', end='')
                node = node.next
            print()


chain = Chaning(13);
chain.put(25, 'grape')
chain.put(37, 'apple')
chain.put(18, 'banana')
chain.put(55, 'cherry')
chain.put(22, 'mango')
chain.put(35, 'lime')
chain.put(50, 'orange')
chain.put(63, 'watermelon')
print('해시테이블:')
chain.print_table()

print('50의 데이터: ', chain.get(50))
print('63의 데이터: ', chain.get(63))
