const fs = require('fs');

let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

let [N, type] = input.shift().split(' ');

type = type.trim();

let playerCount = 0;

let playerSet = new Set();

let result = 0;

input.forEach(name => {
    let player = name.trim();
    if (!playerSet.has(player)) {
        playerSet.add(player);
        playerCount += 1;
    }


    if (type == 'Y' && playerCount == 1) {
        playerCount = 0;
        result += 1;
    }
    else if (type == 'F' && playerCount == 2) {
        playerCount = 0;
        result += 1;
    }
    else if (type == 'O' && playerCount == 3) {
        playerCount = 0;
        result += 1;
    }
})

console.log(result);