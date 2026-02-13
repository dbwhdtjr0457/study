const fs = require('fs');

let input = fs.readFileSync('./input.txt').toString().trim().split('\n')

let numArr = input[1].split(' ').map(Number);

numArr = numArr.sort((a, b) => a - b);

let evenMin = -1;
let oddMin = -1;

let prevEven = -1;
let prevOdd = -1;

for (let i = 0; i < numArr.length; i++) {
    let curr = numArr[i];
    if (curr % 2 == 0) {
        if (prevEven != -1) {
            if (evenMin == -1) evenMin = curr - numArr[prevEven];
            else evenMin = Math.min(evenMin, curr - numArr[prevEven]);
        }

        if (prevOdd != -1) {
            if (oddMin == -1) oddMin = curr - numArr[prevOdd];
            else oddMin = Math.min(oddMin, curr - numArr[prevOdd]);
        }

        prevEven = i;
    }

    else {
        if (prevOdd != -1) {
            if (evenMin == -1) evenMin = curr - numArr[prevOdd];
            else evenMin = Math.min(evenMin, curr - numArr[prevOdd]);
        }

        if (prevEven != -1) {
            if (oddMin == -1) oddMin = curr - numArr[prevEven];
            else oddMin = Math.min(oddMin, curr - numArr[prevEven]);
        }

        prevOdd = i;
    }
}

console.log([evenMin, oddMin].join(' '))