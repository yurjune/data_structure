// ref. https://chamdom.blog/dfs-using-js/

function bfs(graph, start) {
  const queue = [];
  const visited = [];
  const result = [];

  queue.push(start);
  visited[start] = true;
  result.push(start);

  while (queue.length) {
    const node = queue.shift();

    for (const el of graph[node]) {
      if (visited[el]) continue;

      queue.push(el);
      visited[el] = true; // 방문체크는 큐에서 꺼낼 때가 아니라 넣을 때 하자
      result.push(el);
    }
  }

  return result;
}

// 인접 리스트 방식
// 정점이 여러개일때 낮은 정점부터 방문해야 할 경우 오름차순 정렬한다.
const graph = [[1, 2, 4], [0, 5], [0, 5], [4], [0, 3], [1, 2]];

const bfsResult = bfs(graph, 0);
console.log(bfsResult.join(' ')); // 0 1 2 4 5 3
