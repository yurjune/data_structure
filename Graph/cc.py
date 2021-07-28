# 연결성분(connected component) 찾기

def dfs(graph, v, visited):
    visited[v] = True
    cc.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [[3], [6, 10], [7, 11], [0, 6, 8], [13], [14],
[1, 3, 8, 10, 11], [2, 11], [3, 6, 10, 12],
[13], [1, 6, 8], [2, 6, 7], [8], [4, 9], [5]]
visited = [False] * len(graph)
cclist = []

for i in range(len(graph)):
    if not visited[i]:
        cc = []
        dfs(graph, i, visited)
        cclist.append(cc)
print(cclist)
