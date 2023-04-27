# 버블정렬
# 인접한 두 원소를 비교하여 조건에 맞으면 값을 교환하는 정렬

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):    # len(arr)-1 에 주의
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

array = [54, 88, 77, 26, 93, 17, 49, 10, 77, 11, 31, 22, 44, 17, 20]
bubble_sort(array)
print(array)

# ref. https://www.daleseo.com/sort-bubble/
