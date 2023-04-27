// 간선이 양방향으로 연결하는 두 정점의 번호가 주어질 때 그래프 만들기
// N: 정점의 개수, M: 간선의 개수, V: 시작 정점
const [N, M, V] = [4, 5, 1];
const edges = ['1 2', '1 3', '1 4', '2 4', '3 4'];
const graph = [...Array(N + 1)].map(() => []);

for (let i = 0; i < M; i++) {
  const [from, to] = edges[i].split(' ').map(Number);
  graph[from].push(to);
  graph[to].push(from);
}

console.log(graph); // [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
