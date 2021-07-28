# DFS
# 임의의 노드에서 최대로 진입할 수 있는 깊이까지 탐색하고 다시 돌아와 탐색을 수행하는 방식
# 재귀함수 이용

# 그래프 인접리스트
graph = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]
N = len(graph)
visited = [False] * N

def dfs(v):
    visited[v] = True
    print(v, ' ', end='')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


print('DFS 방문 순서: ', end='')
for i in range(N):
    if not visited[i]:
        dfs(i)
