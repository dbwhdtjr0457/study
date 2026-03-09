const fs = require('fs');

let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

let dataLen = Number(input[0]);
let dataArr = input[1].split(' ').map(Number);

let height = 0;

let resultArr = [];
for (let i = 0; i < dataLen; i++) {
    resultArr.push(0);
}

dataArr.forEach(data => {
    height += 1;

    let zeroCount = 0;
    let finalIdx = 0;

    while (zeroCount < data) {
        if (resultArr[finalIdx] == 0) zeroCount += 1;
        finalIdx += 1;
    }

    while (resultArr[finalIdx] != 0) finalIdx += 1;

    resultArr[finalIdx] = height;
})

console.log(resultArr.join(' '));