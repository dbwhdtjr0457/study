const fs = require('fs');

let input = fs.readFileSync("./input.txt").toString().trim().split('\n');

let data = input[1].split(' ').map(Number);

let left = 0;
let right = data.length - 1;

let minNum = data[left] + data[right];
let addNum = data[left] + data[right];

let result = [data[left], data[right]];

while (left < right) {

    addNum = data[left] + data[right];

    if (Math.abs(minNum) > Math.abs(addNum)) {
        result = [data[left], data[right]];
        minNum = addNum;
    }
        if (addNum > 0) {
        right -= 1;
    }
    else if (addNum < 0) {
        left += 1;
    }
    else break;
}

console.log(result.join(' '));