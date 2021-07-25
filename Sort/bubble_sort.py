# 버블정렬
# 인접한 두 수를 비교하여 큰 수를 뒤로 보내는 정렬

def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1, i, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    return array


array = [54, 88, 77, 26, 93, 17, 49, 10, 77, 11, 31, 22, 44, 17, 20]
bubble_sort(array)
print(array)
