const fs = require('fs')

let input = fs.readFileSync("./input.txt").toString().trim().split('\n');

let [N, M] = input.shift().split(" ").map(Number)

input = input.map(Number)

let minNum = Math.max(...input);
let maxNum = input.reduce((acc, val) => acc + val, 0);
let answer = 0;

while (minNum < maxNum) {
    let mid = Math.floor((minNum + maxNum) / 2);

    let sum = 0
    let count = 1

    input.forEach(val => {
        if (sum + val <= mid) {
            sum += val;
        }
        else {
            count += 1
            sum = val;
        }
    })
    
    if (count <= M) {
        answer = mid;
        maxNum = mid - 1;
    }
    else {
        minNum = mid + 1;
    }
}

console.log(minNum);