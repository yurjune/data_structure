class DoubleHashing:    # 이중해싱, 이차조사
    def __init__(self, size):
        self.M = size
        self.slot = [None]*size
        self.data = [None]*size
        self.N = 0  # 저장된 항목 수

    def hash(self, key):
        return key % self.M

    def put(self, key, value):
        initial_index = self.hash(key)
        i = initial_index
        j = 0
        while True:
            if self.slot[i] == None:
                self.slot[i] = key
                self.data[i] = value
                self.N += 1
                return
            if self.slot[i] == key:
                self.data[i] = value
                return
            j += 1
            # 다음 원소 검사: 이차조사
            i = (initial_index + j*j) % self.M
            if self.N > self.M:  # ??
                break

    def get(self, key):
        initial_index = self.hash(key)
        i = initial_index
        j = 0
        while self.slot[i] != None:
            if self.slot[i] == key:
                return self.data[i]
            j += 1
            i = (initial_index + j*j) % self.M
        return None

    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.slot[i])), ' ', end='')
        print()


qp = DoubleHashing(13);
qp.put(25, 'grape')
qp.put(37, 'apple')
qp.put(18, 'banana')
qp.put(55, 'cherry')
qp.put(22, 'mango')
qp.put(35, 'lime')
qp.put(50, 'orange')
qp.put(63, 'watermelon')
print('해시테이블:')
qp.print_table()

print('50의 데이터: ', qp.get(50))
print('63의 데이터: ', qp.get(63))
