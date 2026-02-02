const fs = require('fs');

let input = fs.readFileSync("./input.txt").toString().trim().split('\n');

let goal = Number(input[0].split(' ')[1]);

let data = input[1].split(' ').map(Number);

let [left, right] = [-1, -1];

let addNum = 0;
let len = 0;
let minLen = 0;

while (right < data.length - 1 || left < data.length - 1) {
    if (addNum < goal && right < data.length - 1) {
        right += 1;
        addNum += data[right];
        len += 1;
    }
    else if (left < data.length - 1){
        left += 1;
        addNum -= data[left];
        len -= 1;
    }
    
    if (addNum >= goal) {
        if (len < minLen || minLen == 0) minLen = len;
    }
}

console.log(minLen);