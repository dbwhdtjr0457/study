// const a = {x: {y: 10}};

// const b = {...a};

// console.log(a);
// console.log(b);
// console.log(a === b);
// console.log(a.x === b.x)

// p.201

// function foo() {
//   console.log(x);
//   //var x = 'local'
//   //return x
// }

// foo();

// p.212

// console.log(foo);
// let foo; //ReferenceError: Cannot access 'foo' before initialization

// var person = {
//   name: 'joyoo',
//   age: 24,
//   getInfo: function() {
//     return this.name + this.age;
//   },
//   hobby: {
//     baseball: 'no',
//     'ping-pong': 'yes'
//   }
// }

// var person2 = person;

// console.log(person.name);
// console.log(person.age);
// console.log(person['age'])
// console.log(person.getInfo);
// console.log(person.getInfo());
// console.log(person['getInfo']());
// console.log(person.hobby);

// console.log(person2.name)
// console.log(person2.age)
// console.log(person == person2)
// console.log(person === person2)
// console.log(person.age === person2.age)
// console.log(person2.hobby)
// console.log(person.hobby === person2.hobby)

// const x = {y : {z : 1}}

// const X = {...x};

// console.log(X === x)

// var x = 1;

// function foo() {
//   var x = 10;
//   console.log('global function foo');
// }

// function bar() {
//   function foo() {
//     console.log('local function foo');
//     console.log(x);
//   }

//   foo();
//   for (var x = 0; x < 10; x++) {};
//   console.log(x);
// }

// bar();
// console.log(x);

// let foo = 1;

// {
//   console.log(foo);
//   var foo = 2;
// }

// var weather = {
//   date: '20220727',
//   weather : 'Sunny',
//   getInfo1: () => {
//     console.log(this.date + this.weather)
//   },
//   getInfo2: function () {
//     console.log(this.date + this.weather)
//   }
// }

// weather.getInfo1()
// weather.getInfo2()

// 