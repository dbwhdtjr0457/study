const fs = require('fs');

let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

let num = Number(input[0])


let data = Array.from({length: num}, (_, i) => i + 1);

let head = 0;

while (data.length - head > 1) {
    head += 1;

    data.push(data[head]);
    head += 1;
}

console.log(data[head]);