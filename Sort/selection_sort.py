# 선택정렬
# 항상 정렬되지 않은 부분에서 최솟값을 선택하여 정렬되지 않은 부분 가장 왼쪽 원소와 교환

def selection_sort(array):
    for i in range(0, len(array)-1):
        minimum = i
        for j in range(i, len(array)):
            # 정렬되지 않은 부분에서 최솟값 선택
            if array[minimum] > array[j]:
                minimum = j
        # 현재 원소와 최솟값 원소 교환
        array[i], array[minimum] = array[minimum], array[i]


array = [54, 88, 77, 26, 93, 17, 49, 10, 77, 11, 31, 22, 44, 17, 20]
selection_sort(array)
print(array)
