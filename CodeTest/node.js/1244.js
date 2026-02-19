const fs = require("fs");

let input = fs.readFileSync('./input.txt').toString().split('\n').map(line => line.trim())

input.shift();
let data = input.shift().split(' ').map(Number);
data.unshift(-1);

input.shift();

function switchBit(idx) {
    if (data[idx] == 1) data[idx] = 0;
    else if (data[idx] == 0) data[idx] = 1;
}

input.forEach((line) => {
    let [sex, idx] = line.split(' ').map(Number);

    if (sex == 1) {
        data.forEach((_, i) => {
            if (i > 0 && i % idx == 0) {
                switchBit(i);
            }
        })
    }
    if (sex == 2) {
        switchBit(idx);

        let temp = 0;
        while (true) {
            temp += 1;
            if (idx + temp <= data.length - 1 && idx - temp >= 0 && data[idx + temp] == data[idx - temp]) {
                switchBit(idx + temp);
                switchBit(idx - temp);
            }
            else break;
        }
    }
}) 
data.shift();

let i = 0;

while (data.length >= i * 20) {
    console.log(data.slice(i * 20, (i + 1) * 20).join(' '));
    i += 1;
}