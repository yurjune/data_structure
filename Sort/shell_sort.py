# 쉘 정렬

def shell_sort(array):
    h = 4   # 3x+1 간격: 1, 4, 13, 40, 121 중에서 4와 1만 사용
    while h >= 1:
        for i in range(h, len(array)):
            j = i
            while j >= h and array[j] < array[j-h]:
                array[j], array[j-h] = array[j-h], array[j]
                j -= h
        h //= 3  # 간격(h값)을 줄여가며 정렬 수행

array = [54, 88, 77, 26, 93, 17, 49, 10, 77, 11, 31, 22, 44, 17, 20]
shell_sort(array)
print(array)
