const fs = require("fs");

const input = fs.readFileSync("./input.txt").toString().trim();

const inputList = input.split("\n");

const [N, M, X] = inputList[0].split(" ").map((i) => Number(i));

const graph = Array.from({ length: N + 1 }, () => []);
const reverseGraph = Array.from({ length: N + 1 }, () => []);

for (let i = 1; i < M + 1; i++) {
  const [start, end, T] = inputList[i].split(" ").map((i) => Number(i));

  graph[start].push([end, T]);
  reverseGraph[end].push([start, T]);
}
