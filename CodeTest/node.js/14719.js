const fs = require("fs");

let input = fs.readFileSync("./input.txt").toString().trim().split('\n');

let data = input[1].split(' ').map(Number);

let result = 0;

for (let i = 1; i < data.length - 1; i++) {
    let leftData = data.slice(0, i);
    let rightData = data.slice(i + 1);

    let leftMax = Math.max(...leftData);
    let rightMax = Math.max(...rightData);

    result += Math.max(0, Math.min(leftMax, rightMax) - data[i]);
}

console.log(result);