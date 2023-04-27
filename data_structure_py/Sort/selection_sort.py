# 선택정렬
# 항상 정렬되지 않은 부분에서 최솟값을 선택하여 정렬되지 않은 부분 가장 왼쪽 원소와 교환

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


array = [54, 88, 77, 26, 93, 17, 49, 10, 77, 11, 31, 22, 44, 17, 20]
selection_sort(array)
print(array)
