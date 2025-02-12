const fs = require("fs");

const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")
  .map((line) => line.trim());

const numList = input[1].split(" ").map((num) => parseInt(num));

const result = numList.reduce((prev, now) => {
  if (now === 1) return prev;
  const temp = Math.floor(Math.sqrt(now));
  for (let i = 2; i <= temp; i++) if (now % i == 0) return prev;
  return prev + 1;
}, 0);

console.log(result);
