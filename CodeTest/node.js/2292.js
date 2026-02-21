const fs = require('fs');

let input = fs.readFileSync('./input.txt').toString().trim();

let num = Number(input);

let sum = 1;

if (num == 1) console.log(1);
else {
    for (let i = 0; sum < num; i++) {
        sum += i * 6;

        if (sum >= num) console.log(i + 1);
    }
}