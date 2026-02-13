const fs = require('fs');

let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

let [H, W, N, M] = input[0].split(' ').map(Number);


let col = Math.floor(H / (N + 1));
if (H % (N + 1) > 0) col += 1;


let row = Math.floor(W / (M + 1));
if (W % (M + 1) > 0) row += 1;


console.log(col * row);