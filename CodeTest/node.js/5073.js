const fs = require("fs")

let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

input.forEach(line => {
    let arr = line.split(' ').map(Number);

    if (arr[0] != 0 && arr[1] != 0 && arr[2] != 0) {
        arr = arr.sort((a, b) => a - b);

        if (arr[0] + arr[1] <= arr[2]) console.log('Invalid');
        else {
            if (arr[0] == arr[1] && arr[1] == arr[2]) console.log('Equilateral');
            else if (arr[0] == arr[1] || arr[1] == arr[2] || arr[2] == arr[0]) console.log('Isosceles');
            else console.log('Scalene');
        }
    }
})