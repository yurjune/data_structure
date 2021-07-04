class BHeap:  # 최소힙
    def __init__(self, array):
        self.array = array  # array = [None]*1
        self.N = len(array)-1  # 첫 항목은 항상 None

    def create_heap(self):
        for i in range(self.N // 2, 0, -1):
            self.down_heap(i)

    def insert(self, item):
        self.array.append(item)  # a.append([30, 'grape'])
        self.N += 1
        self.up_heap(self.N)

    def delete_min(self):
        if self.N == 0:
            print("비어 있음")
            return None
        minimum = self.array[1]
        self.array[1], self.array[-1] = self.array[-1], self.array[1]
        del self.array[-1]
        self.N -= 1
        self.down_heap(1)
        return minimum

    def down_heap(self, i):
        while 2*i <= self.N:
            k = 2*i  # 왼쪽 자식
            # 자식 승자(더 작은 쪽) 정하기
            if k < self.N and self.array[k][0] > self.array[k+1][0]:
                k += 1
            # 부모보다 자식이 크면 힙속성 만족
            if self.array[i][0] < self.array[k][0]:
                break
            # 부모가 자식보다 크면 자리 교환
            self.array[i], self.array[k] = self.array[k], self.array[i]
            i = k   # 레벨 내려가기

    def up_heap(self, j):
        # [j]: 자식, [j//2]: 부모
        while j > 1 and self.array[j//2][0] > self.array[j][0]:
            self.array[j], self.array[j//2] = self.array[j//2], self.array[j]
            j = j//2    # 레벨 올라가기

    def print_heap(self):
        for i in range(1, self.N+1):
            print('[%2d' % self.array[i][0], self.array[i][1], ']', end='')
        print(f'\n힙 크기 = {self.N}\n')
