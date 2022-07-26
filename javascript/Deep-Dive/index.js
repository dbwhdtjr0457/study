const a = {x: {y: 10}};

const b = {...a};

console.log(a);
console.log(b);
console.log(a === b);
console.log(a.x === b.x)