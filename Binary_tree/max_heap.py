class MaxHeap:
    def __init__(self, array):
        self.array = array
        self.N = len(array)-1

    def create_heap(self):
        for i in range(self.N//2, 0, -1):
            self.down_heap(i)

    def insert(self, key_value):
        self.array.append(key_value)  # array.append([30, 'grape'])
        self.N += 1
        self.up_heap(self.N)

    def delete_max(self):
        if self.N == 0:
            print("비어 있음")
            return None
        maximum = self.array[1]
        self.array[1], self.array[-1] = self.array[-1], self.array[1]
        del self.array[-1]
        self.N -= 1
        self.down_heap(1)
        return maximum

    def down_heap(self, i):
        while 2*i <= self.N:
            k = 2*i  # 왼쪽 자식
            if k < self.N and self.array[k][0] < self.array[k+1][0]:
                k += 1
            if self.array[i][0] > self.array[k][0]:
                break
            self.array[i], self.array[k] = self.array[k], self.array[i]
            i = k

    def up_heap(self, j):
        # [j]: 자식, [j//2]: 부모
        while j > 1 and self.array[j//2][0] < self.array[j][0]:
            self.array[j], self.array[j//2] = self.array[j//2], self.array[j]
            j //= 2

    def print_heap(self):
        for i in range(1, self.N+1):
            print('[%2d' % self.array[i][0], self.array[i][1], ']', end='')
        print(f'\n힙 크기 = {self.N}\n')


array = [None]*1
array.append([90, 'watermelon'])
array.append([80, 'pear'])
array.append([70, 'melon'])
array.append([50, 'lime'])
array.append([60, 'mango'])
array.append([20, 'cherry'])
array.append([30, 'grape'])
array.append([35, 'orange'])
array.append([10, 'apricot'])
array.append([15, 'banana'])
array.append([45, 'lemon'])
array.append([40, 'kiwi'])

maxheap = MaxHeap(array)
maxheap.create_heap()
print("최대 힙:")
maxheap.print_heap()