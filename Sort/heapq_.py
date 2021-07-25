import heapq
array = [54, 88, 77, 26, 93, 17, 49, 10, 77, 11, 31, 22, 44, 17, 20]

heapq.heapify(array)
data = []
while array:
    data.append(heapq.heappop(array))
print(data)
