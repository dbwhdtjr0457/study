const fs = require("fs");

let input = fs.readFileSync("./input.txt").toString().trim().split('\n');

let towers = input[1].split(' ').map(Number)

let stack = [];

let result = [];

towers.forEach((height, index) => {
    for (let i = stack.length - 1; i >= 0; i--) {

        if (stack[i][0] < height) stack.pop();
        else break;
    }

    stack.push([height, index + 1])

    if (stack.length == 1) result.push(0);
    else result.push(stack[stack.length - 2][1])
});

console.log(result.join(' ').trim())