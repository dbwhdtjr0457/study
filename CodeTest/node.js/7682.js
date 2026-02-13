const fs = require("fs");

let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

const winPatterns = [
    [0, 1, 2],  
    [3, 4, 5], 
    [6, 7, 8], 
    [0, 3, 6], 
    [1, 4, 7], 
    [2, 5, 8],
    [0, 4, 8], 
    [2, 4, 6]
];

function isWin(line, player) {
    let flag = false;

    winPatterns.forEach(pattern => {
        let isWinPattern = true;
        pattern.forEach(idx => {
            if (line[idx] != player) isWinPattern = false;
        })

        if (isWinPattern == true) flag = true;
    })

    return flag;
}

input.forEach(line => {
    if (line != 'end') {
        let countX = line.split('X').length - 1;
        let countO = line.split('O').length - 1;

        if (countX != countO && countX != countO + 1) console.log('invalid');
        else if (isWin(line, 'X')) {
            if (countX == countO + 1 && !isWin(line, 'O')) console.log('valid');
            else console.log('invalid');
        }
        else if (isWin(line, 'O')) {
            if (countX == countO && !isWin(line, 'X')) console.log('valid');
            else console.log('invalid');
        }
        else if (countX == 5 && countO == 4) console.log('valid');
        else console.log('invalid');
    }
})
