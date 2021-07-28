# BFS
# 임의의 노드에서 시작하여 인접한 노드를 모두 확인한 후 다음 depth를 탐색
# 큐 자료구조 활용

graph = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]
N = len(graph)
visited = [False] * N


def bfs(start):
    queue = []
    queue.append(start)
    visited[start] = True
    while len(queue) != 0:
        v = queue.pop(0)
        print(v, '', end='')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

print('BFS 방문 순서: ', end='')
for i in range(N):
    if not visited[i]:
        bfs(i)
