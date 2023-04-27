# BFS
# 임의의 노드에서 시작하여 인접한 노드를 모두 확인한 후 다음 depth를 탐색
# 큐 자료구조 활용
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]
visited = [False] * len(graph)

for i in range(len(graph)):
    if not visited[i]:
        bfs(graph, i, visited)  # 0 2 1 3 9 8 4 5 7 6
