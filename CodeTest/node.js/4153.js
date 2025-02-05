const fs = require("fs");

let input = fs.readFileSync("/dev/stdin").toString().split("\n");

for (let i = 0; i < input.length; i++) {
  let newList = input[i].split(" ").map((number) => {
    return parseInt(number.trim());
  });

  newList.sort((a, b) => a - b);

  let [A, B, C] = newList;

  if (A === 0 && B === 0 && C === 0) break;

  if (A ** 2 + B ** 2 == C ** 2) console.log("right");
  else console.log("wrong");
}
