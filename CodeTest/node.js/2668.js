const fs = require("fs");

let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

input = input.map(Number);

let visited = new Array(input.length).fill(false);

visited[0] = true;

resultArr = [];

function search(v, graph = []) {
    visited[v] = true;

    graph.push(v);

    let vIdx = graph.indexOf(input[v]);

    if (vIdx != -1) {
        graph.slice(vIdx).forEach(v => {
            resultArr.push(v)
        })
    }
    else if (!visited[input[v]]){
        search(input[v], graph);
    }
}


input.forEach((v, idx) => {
    if (!visited[idx]) {
        search(idx);
    }
})

console.log(resultArr.length);
console.log(resultArr.sort((a, b) => a - b).join('\n'));