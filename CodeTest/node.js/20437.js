const fs = require("fs")

let input = fs.readFileSync("./input.txt").toString().trim().split('\n');

input.shift();

while(input.length > 0) {
    let str = input.shift();
    let count = Number(input.shift());

    let alphaData = {};

    [...str.trim()].forEach((alpha, idx) => {
        if (!(alpha in alphaData)) {
            alphaData[alpha] = [];
        }

        alphaData[alpha].push(idx);
    })

    let minRes = -1;
    let maxRes = -1;

    for (const key in alphaData) {
        if (alphaData[key].length >= count) {
            for (let i = 0; i < alphaData[key].length - count + 1; i++) {
                let j = i + count - 1;
                let left = alphaData[key][i];
                let right = alphaData[key][j];

                if (minRes > right - left + 1 || minRes < 0) minRes = right - left + 1;
                if (maxRes < right - left + 1 || maxRes < 0) maxRes = right - left + 1;
            }
        }
    }

    if (minRes < 0 || maxRes < 0) console.log(-1);
    else console.log(minRes, maxRes);
}