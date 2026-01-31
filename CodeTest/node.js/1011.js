const fs = require("fs");

let input = fs.readFileSync("./input.txt").toString().trim().split("\n");

input = input.map(line => line.split(" ").map(Number));

input.shift();

let answers = [];

input.forEach(line => {
    let [start, end] = line;

    let diff = end - start;


    let max = Math.floor(Math.sqrt(diff));

    if (diff == 0) answers.push(0);

    else if (diff == Math.pow(max, 2)) answers.push(2 * max - 1);

    else if (diff <= Math.pow(max, 2) + max) answers.push(2 * max);

    else answers.push(2 * max + 1);
})

console.log(answers.join("\n"));