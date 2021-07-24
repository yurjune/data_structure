# 삽입정렬
# 정렬 되지 않은 부분의 가장 왼쪽 원소를 정렬된 부분에 삽입

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]

array = [54, 88, 77, 26, 93, 17, 49, 10, 77, 11, 31, 22, 44, 17, 20]
insertion_sort(array)
print(array)
