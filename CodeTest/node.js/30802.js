const fs = require("fs");

let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const N = parseInt(input[0]);

const sizeList = input[1].split(" ").map((number) => parseInt(number));

const [T, P] = input[2].split(" ").map((number) => parseInt(number));

const setCount = sizeList.reduce((prev, now) => {
  const newNow = Math.floor(now / T) + (now % T > 0);

  return prev + newNow;
}, 0);

console.log(setCount);

console.log(Math.floor(N / P), N % P);
