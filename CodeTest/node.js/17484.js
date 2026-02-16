const fs = require('fs');

const input = fs.readFileSync(0, 'utf8').trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const board = input.slice(1).map((line) => line.split(' ').map(Number));

const INF = Number.MAX_SAFE_INTEGER;
// dir: 0 => down-left (dc = -1), 1 => down (dc = 0), 2 => down-right (dc = +1)
const dc = [-1, 0, 1];

const dp = Array.from({ length: N }, () =>
  Array.from({ length: M }, () => Array(3).fill(INF))
);

for (let c = 0; c < M; c++) {
  for (let d = 0; d < 3; d++) {
    dp[0][c][d] = board[0][c];
  }
}

for (let r = 1; r < N; r++) {
  for (let c = 0; c < M; c++) {
    for (let d = 0; d < 3; d++) {
      const prevCol = c - dc[d];
      if (prevCol < 0 || prevCol >= M) continue;

      let bestPrev = INF;
      for (let pd = 0; pd < 3; pd++) {
        if (pd === d) continue;
        if (dp[r - 1][prevCol][pd] < bestPrev) {
          bestPrev = dp[r - 1][prevCol][pd];
        }
      }

      if (bestPrev !== INF) {
        dp[r][c][d] = board[r][c] + bestPrev;
      }
    }
  }
}

let answer = INF;
for (let c = 0; c < M; c++) {
  for (let d = 0; d < 3; d++) {
    if (dp[N - 1][c][d] < answer) answer = dp[N - 1][c][d];
  }
}

console.log(answer);
