const fs = require('fs');

let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

input.shift();
input = input.map(word => word.trim());

let result = '';

// 1. KBS1 인덱스 찾기
let kbs1Idx = input.indexOf('KBS1');

input = [input[kbs1Idx], ...input.slice(0, kbs1Idx), ...input.slice(kbs1Idx + 1, input.length)]

result += '1'.repeat(kbs1Idx) + '4'.repeat(kbs1Idx);

// 2. KBS2 인덱스 찾기
let kbs2Idx = input.indexOf('KBS2');

result += '1'.repeat(kbs2Idx) + '4'.repeat(kbs2Idx - 1);

console.log(result);