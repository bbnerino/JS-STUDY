function solution(n) {
  var graph = [];
  for (let i = 0; i < n ; i++) {
    graph.push(new Array(n).fill(0));
  }

  const dy = [0, 1, 0, -1];
  const dx = [1, 0, -1, 0];
  let dir = 0;
  let start = [0, 0];
  graph[0][0] = 1;
  let num = 2;
  while (num <= n ** 2) {
    const ny = dy[dir] + start[0];
    const nx = dx[dir] + start[1];
    if (0 <= ny && ny < n &&  0 <= nx && nx < n) {
      if (graph[ny][nx] === 0) {
        graph[ny][nx] = num;
        num += 1;
        start = [ny, nx];
        continue;
      }
    }
    dir = (dir + 1) % 4;
  }
  return graph;
}
solution(4);
