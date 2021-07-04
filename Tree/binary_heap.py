class BHeap:  # 최소 힙 구현
    def __init__(self, array):
        self.array = array  # array = [None]*1 로 선언
        self.N = len(array) - 1  # 항목수: 첫 항목이 None: 크기 1 감소

    def create_heap(self):  # 데이터를 최소힙으로 정렬
        for i in range(self.N // 2, 0, -1):  # 항목수의 절반만 시행
            self.down_heap(i)

    def insert(self, item):
        # 데이터 추가 방식: a.append([30, 'grape'])
        self.array.append(item)
        self.N += 1
        self.up_heap(self.N)

    def delete_min(self):   # 최솟값(루트) 삭제
        if self.N == 0:
            print("비어 있음")
            return None
        minimum = self.array[1]
        # 루트와 마지막 노드의 자리교환
        self.array[1], self.array[-1] = self.array[-1], self.array[1]
        del self.array[-1]
        self.N -= 1
        self.down_heap(1)   # 루트를 내린다
        return minimum

    def down_heap(self, i):
        while 2*i <= self.N:
            k = 2*i  # k는 왼쪽 자식
            # 자식 중 값이 더 작은쪽과 교환하려한다
            # 자식 승자(더 작은 쪽) 정하기
            if k < self.N and self.array[k][0] > self.array[k+1][0]:
                k += 1
            # 부모보다 자식이 크면 힙속성을 만족하므로 탈출
            if self.array[i][0] < self.array[k][0]:
                break
            # 부모가 더 크면 자식 승자와 자리 교환
            self.array[i], self.array[k] = self.array[k], self.array[i]
            i = k   # 한 층 내려가서 다시 down_heap 수행

    def up_heap(self, j):
        # [j]가 자식일때 [j//2]는 부모가 된다
        while j > 1 and self.array[j//2][0] > self.array[j][0]:  # 부모가 더 크면 자리교환
            # 부모와 자식 교환
            self.array[j], self.array[j//2] = self.array[j//2], self.array[j]
            j = j//2    # 한 층 올라가서 다시 up_heap 수행

    def print_heap(self):
        for i in range(1, self.N+1):
            print('[%2d' % self.array[i][0], self.array[i][1], ']', end='')
        print(f'\n힙 크기 = {self.N}\n')
