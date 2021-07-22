# 해싱: 키를 간단한 해시함수로 계산한 값을 1차원 리스트의 인덱스로 이용하여 항목을 저장하고
# 탐색, 삽입 삭제 연산을 평균 O(1) 시간에 지원하는 자료구조

# 개방주소 방식(open addressing)
class LinearProbing:
    def __init__(self, size):
        self.M = size
        self.slot = [None]*size
        self.data = [None]*size

    def hash(self, key):
        return key % self.M  # 나눗셈 해시함수

    def put(self, key, value):
        initial_index = self.hash(key)
        i = initial_index
        j = 0
        while True:
            # 해시테이블이 비어있다면 삽입
            if self.slot[i] == None:
                self.slot[i] = key
                self.data[i] = value
                return
            # 이미 키가 있다면 데이터만 갱신
            if self.slot[i] == key:
                self.data[i] = value
                return
            # 순차탐색으로 empty 원소 찾기
            j += 1
            i = (initial_index + j) % self.M
            # 초기 위치로 돌아오면 저장 실패
            if i == initial_index:
                break

    def get(self, key):
        initial_index = self.hash(key)
        i = initial_index
        j = 0
        while self.slot[i] != None:
            if self.slot[i] == key:
                return self.data[i]
            j += 1
            i = (initial_index + j) % self.M
            if i == initial_index:
                return None
        return None

    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.slot[i])), ' ', end='')
        print()


lp = LinearProbing(13);
lp.put(25, 'grape')
lp.put(37, 'apple')
lp.put(18, 'banana')
lp.put(55, 'cherry')
lp.put(22, 'mango')
lp.put(35, 'lime')
lp.put(50, 'orange')
lp.put(63, 'watermelon')
print('해시테이블:')
lp.print_table()

print('50의 데이터: ', lp.get(50))
print('63의 데이터: ', lp.get(63))
