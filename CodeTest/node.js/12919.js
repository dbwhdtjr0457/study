const fs = require("fs");

let input = fs.readFileSync("./input.txt").toString().trim().split('\n');

let start = input[0].trim();
let end = input[1].trim();

function findWay(str) {
    if (str.length <= start.length) {
        if (str == start) return 1;
        else return 0;
    }
    let strArr = str.split('');

    if (strArr[strArr.length - 1] == 'A' && findWay(str.slice(0, str.length - 1)) == 1) return 1;

    if (strArr[0] == 'B' && findWay(strArr.slice(1).reverse().join('')) == 1) return 1;

    else return 0;
}

console.log(findWay(end));