# DFS
# 임의의 노드에서 최대로 진입할 수 있는 깊이까지 탐색하고 다시 돌아와 탐색을 수행하는 방식
# 재귀함수 이용

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)  # 재귀


graph = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]
visited = [False] * len(graph)

for i in range(len(graph)):  # 연결성분이 2개 이상일 수 있으므로
    if not visited[i]:
        dfs(graph, i, visited)  # 0 2 3 9 8 1 4 5 7 6
