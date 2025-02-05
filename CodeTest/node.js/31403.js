const fs = require("fs");

let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let A = input[0].trim();
let B = input[1].trim();
let C = input[2].trim();

console.log(parseInt(A) + parseInt(B) - parseInt(C));
console.log(A + B - C);
