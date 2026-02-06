const fs = require("fs");

let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

let [N, K] = input[0].split(' ').map(Number);


visited = new Set();

let queue = [];

visited.add(N);
queue.push([N, 0]);

while (queue.length > 0) {
    let value = queue.shift();
    if (value[0] == K) {
        console.log(value[1]);
        return;
    }
    else {
        if (value[0] * 2 <= 100000 && !visited.has(value[0] * 2)) {
            visited.add(value[0] * 2);
            queue.unshift([value[0] * 2, value[1]]);
        }
        if (value[0] - 1 >= 0 && !visited.has(value[0] - 1)) {
            visited.add(value[0] - 1);
            queue.push([value[0] - 1, value[1] + 1]);
        }
        if (value[0] + 1 <= 100000 && !visited.has(value[0] + 1)) {
            visited.add(value[0] + 1);
            queue.push([value[0] + 1, value[1] + 1]);
        } 
    }
}