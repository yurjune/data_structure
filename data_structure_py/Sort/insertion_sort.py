# 삽입정렬
# 정렬되지 않은 부분의 가장 왼쪽 원소를 정렬된 부분의 원소와 비교하여 적절한 위치에 삽입하는 정렬

def insertion_sort(arr):
    for i in range(1, len(arr)):  # 두 번째 요소부터 삽입
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

array = [54, 88, 77, 26, 93, 17, 49, 10, 77, 11, 31, 22, 44, 17, 20]
insertion_sort(array)
print(array)
