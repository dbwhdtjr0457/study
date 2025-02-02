const fs = require("fs");

// let input = fs.readFileSync("/dev/stdin").toString().trim();
let input = fs.readFileSync("./input.txt").toString().split("-");

for (let i = 0; i < input.length; i++) {
  console.log(i);
}
