import random

class RandomProbing:
    def __init__(self, size):
        self.M = size
        self.slot = [None]*size
        self.data = [None]*size
        self.N = 0

    def hash(self, key):
        return key % self.M

    def put(self, key, value):
        initial_index = self.hash(key)
        i = initial_index
        random.seed(1000)
        while True:
            if self.slot[i] == None:
                self.slot[i] = key
                self.data[i] = value
                return
            if self.slot[i] == key:
                self.data[i] = value
                return
            j = random.randint(1, 99)
            i = (initial_index + j) % self.M
            if self.N > self.M:
                break

    def get(self, key):
        initial_index = self.hash(key)
        i = initial_index
        random.seed(1000)
        while self.slot[i] != None:
            if self.slot[i] == key:
                return self.data[i]
            j = random.randint(1, 99)
            i = (initial_index + j) % self.M
        return None

    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.slot[i])), ' ', end='')
        print()


rp = RandomProbing(13);
rp.put(25, 'grape')
rp.put(37, 'apple')
rp.put(18, 'banana')
rp.put(55, 'cherry')
rp.put(22, 'mango')
rp.put(35, 'lime')
rp.put(50, 'orange')
rp.put(63, 'watermelon')
print('해시테이블:')
rp.print_table()

print('50의 데이터: ', rp.get(50))
print('63의 데이터: ', rp.get(63))
