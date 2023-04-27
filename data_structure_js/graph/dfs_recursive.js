function dfs(graph, node, visited, result) {
  visited[node] = true;
  result.push(node);

  for (const el of graph[node]) {
    if (visited[el]) continue;
    dfs(graph, el, visited, result);
  }

  return result;
}

const graph = [[1, 2, 3], [0, 6], [0], [0, 4, 5], [3], [3], [1]];
const visited = [];
const result = [];

const dfsResult = dfs(graph, 0, visited, result);
console.log(dfsResult.join(' ')); // 0 1 6 2 3 4 5
