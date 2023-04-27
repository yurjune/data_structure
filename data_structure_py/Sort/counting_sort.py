def counting_sort(arr):
    # 원소의 최댓값 까지 인덱스로 사용할 수 있도록 베열의 길이를 최댓값+1 로 설정
    count = [0] * (max(arr) + 1)

    for num in arr:
        count[num] += 1

    # 배열의 원소를 누적합으로 갱신 (arr의 원소를 정렬된 위치에 바로 삽입하기 위해)
    for i in range(1, len(count)):
        count[i] += count[i-1]

    result = [0] * (len(arr))
    for num in arr:
        idx = count[num] - 1
        result[idx] = num
        count[num] -= 1
    return result

array = [54, 88, 77, 26, 93, 17, 49, 10, 77, 11, 31, 22, 44, 17, 20]
result = counting_sort(array)
print(result)
