# 병합정렬
# 크기가 N인 리스트를 N/2로 분할하여 재귀적으로 병합정렬한 후 다시 병합하여 정렬

def merge_sort(array):
    if len(array) <= 1:  # 재귀 종료
        return array

    # 분할하여 병합정렬
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left_part = merge_sort(left)
    right_part = merge_sort(right)
    return merge(left_part, right_part)


def merge(left, right):
    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


array = [54, 88, 77, 26, 93, 17, 49, 10, 77, 11, 31, 22, 44, 17, 20]
result = merge_sort(array)
print(result)
