# DFS
# 임의의 노드에서 최대로 진입할 수 있는 깊이까지 탐색하고 다시 돌아와 탐색을 수행하는 방식
# 재귀함수 이용

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)  # 재귀

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9

dfs(graph, 1, visited)
