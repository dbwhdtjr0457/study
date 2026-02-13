const fs = require("fs");

let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

let [maxHeight, maxDigit, maxChange, currHeight] = input[0].split(' ').map(Number);

let pTable = [
    [0, 4, 3, 3, 4, 3, 2, 3, 1, 2], 
    [4, 0, 5, 3, 2, 5, 6, 1, 5, 4], 
    [3, 5, 0, 2, 5, 4, 3, 4, 2, 3], 
    [3, 3, 2, 0, 3, 2, 3, 2, 2, 1], 
    [4, 2, 5, 3, 0, 3, 4, 3, 3, 2], 
    [3, 5, 4, 2, 3, 0, 1, 4, 2, 1], 
    [2, 6, 3, 3, 4, 1, 0, 5, 1, 2], 
    [3, 1, 4, 2, 3, 4, 5, 0, 4, 3], 
    [1, 5, 2, 2, 3, 2, 1, 4, 0, 1], 
    [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]
]

let result = 0;

function backTracking(idx, leftChange, numStr) {
    if (idx == maxDigit){
        if (Number(numStr) <= maxHeight && Number(numStr) >= 1 && Number(numStr) != currHeight) {
            result += 1;
        }
        return;
    }

    let currIdxNum = Number((new Array(maxDigit - String(currHeight).length).fill('0').join('') + String(currHeight))[idx]);
    pTable[currIdxNum].forEach((diff, i) => {
        if (leftChange >= diff) {
            backTracking(idx + 1, leftChange - diff, numStr + String(i))
        }
    })
}

backTracking(0, maxChange, '');

console.log(result);