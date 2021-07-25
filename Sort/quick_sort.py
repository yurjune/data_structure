# 퀵정렬
# 리스트의 한 원소(피벗)를 기준으로 피벗보다 작은원소들과 큰 원소들을 각각 피벗의 좌우로 분할하여 각각 재귀적으로 정렬

def quick_sort(array):
    if len(array) < 2:
        return array

    pivot = array[0]
    left = [i for i in array[1:] if i <= pivot]  # 피벗과 같은 값이 사라지는 것을 방지
    right = [i for i in array[1:] if i > pivot]
    result = quick_sort(left) + [pivot] + quick_sort(right)
    return result


array = [54, 88, 77, 26, 93, 17, 49, 10, 77, 11, 31, 22, 44, 17, 20]
result = quick_sort(array)
print(result)
