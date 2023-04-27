# 힙정렬: 최대힙을 이용하여 정렬

def heap_sort(array):
    def create_heap(array):
        heap_size = len(array) - 1
        for i in range(heap_size // 2, 0, -1):
            down_heap(i, heap_size)

    def down_heap(i, size):
        while 2*i <= size:
            k = 2*i  # 왼쪽 자식
            if k < size and array[k] < array[k+1]:
                k += 1
            if array[i] > array[k]:
                break
            array[i], array[k] = array[k], array[i]
            i = k

    create_heap(array)
    heap_size = len(array) - 1
    for i in range(heap_size):
        array[1], array[heap_size] = array[heap_size], array[1]
        down_heap(1, heap_size-1)   # heap_size-1: 정렬된 노드 제외하고 힙정렬 수행
        heap_size -= 1

array = [None, 54, 88, 77, 26, 93, 17, 49, 10, 77, 11, 31, 22, 44, 17, 20]
heap_sort(array)
print(array)
