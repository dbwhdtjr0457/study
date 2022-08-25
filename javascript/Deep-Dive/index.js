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

// p.249

// const increase = function (num) 
// {
//     return ++num;
// };

// const decrease = function (num)
// {
//     return --num;
// };

// const auxs = {increase, decrease};

// function makeCounter(aux) 
// {
//     let num = 0;

//     return function()
//     {
//         num = aux(num);
//         return num;
//     };
// }

// const increaser = makeCounter(auxs.increase);
// console.log(increaser()); // 1
// console.log(increaser()); // 2

// p. 254

// function sum() {
//     let res = 0;

//     for (let i = 0; i < arguments.length; i++) {
//         res += arguments[i];
//     }

//     return res;
// }

// console.log(sum()); // 0
// console.log(sum(1, 2)); // 3
// console.log(sum(1, 2, 3)); // 6

// p. 263

// function Circle(radius) {
//     this.radius = radius;
// }

// // Circle 생성자 함수가 생성한 모든 인스턴스가 getArea 메서드를
// // 공유해서 사용할 수 있도록 프로토타입에 추가한다.
// Circle.prototype.getArea = function () {
//     return Math.PI * this.radius ** 2;
// }


// p. 277

// console.log(Person);

// console.log(Person("Hi"));

// function Person(name) {
//     this.name = name;
//     return (name);
// }

// // p.300

// //프로토타입이 null인 객체 생성.
// // obj -> null
// let obj = Object.create(null);
// console.log(Object.getPrototypeOf(obj) == null); // true
// // Object.prototype을 상속받지 못한다.
// //console.log(obj.toString()); -> TypeError

// // obj -> Object.prototype -> null
// // obj = {};와 동일하다.
// obj = Object.create(Object.prototype);
// console.log(Object.getPrototypeOf(obj) == Object.prototype); // true

// // obj => Object.prototype -> null
// // obj = { x: 1 };와 동일하다.
// obj = Object.create(Object.prototype, {
//     x: {value: 1, writable: true, enumerable: true, configurable: true}
// });
// // 위 코드는 아래와 동일하다.
// // obj = Object.create(Object.prototype);
// // obj.x = 1;
// console.log(obj.x); // 1
// console.log(Object.getPrototypeOf(obj) === Object.prototype); // true

// const myProto = { x: 10 };
// // 임의의 객체를 직접 상속받는다.
// // obj -> myProto -> Object.prototype -> null
// obj = Object.create(myProto);
// console.log(obj.x);
// console.log(Object.getPrototypeOf(obj) === myProto); // true

// // 생성자 함수
// function Person(name) {
//     this.name = name
// }

// // obj -> person.prototype -> Object.prototype -> null
// // obj = new Person('Lee')와 동일하다.
// obj = Object.create(Person.prototype);
// obj.name = 'Lee';
// console.log(obj.name); // Lee
// console.log(Object.getPrototypeOf(obj) === Person.prototype); // true

// p. 226

// const person = {};

// Object.defineProperty(person, 'firstName', {
//     value: 'Ungmo',
//     writable: true,
//     enumerable: true,
//     configurable: true
// });

// Object.defineProperty(person, 'lastName', {
//     value: 'Lee'
// });

// let descriptor = Object.getOwnPropertyDescriptor(person, 'firstName');
// console.log('firstName', descriptor);

// descriptor = Object.getOwnPropertyDescriptor(person, 'lastName');
// console.log('lastName', descriptor);



// console.log(Object.keys(person));

// person.lastName = 'Kim';

// delete person.lastName;

// descriptor = Object.getOwnPropertyDescriptor(person, 'lastName');
// console.log('lastName', descriptor);

// Object.defineProperty(person, 'fullName', {
//     get() {
//         return `${this.firstName} ${this.lastName}`;
//     },

//     set(name) {
//         [this.firstName, this.lastName] = name.split(' ');
//     },
//     enumerable: true,
//     configurable: true
// });

// descriptor = Object.getOwnPropertyDescriptor(person, 'fullName');
// console.log('fullName', descriptor);

// person.fullName = 'Heegun Kim';
// descriptor = Object.getOwnPropertyDescriptor(person, 'lastName');
// console.log('lastName', descriptor)
// console.log(person);

// function Circle(radius) {
//     // // new.target
//     // if (!new.target) {
//     //     return new Circle(radius);
//     // }
//     // // 스코프 세이프
//     // if (!(this instanceof Circle)) {
//     //     return new Circle(radius);
//     // }

//     this.radius = radius;
//     this.getDiameter = function() {
//         return 2 * this.radius;
//     };
// }

// p.249

// const CircleDiameter = function (radius) {
//     return 2 * radius;
// }

// function CircleInfo()

// const func = Function("x", "return x * x");
// console.log(typeof func);

// p.313

// function foo() {
//     x = 10;
// }
// foo();

// console.log(x); // 10

// p.317

// (function() {
//     'use strict';

//     var x = 1;
//     delete x; // SyntaxError: Delete of an unqualifed identifier in strict mode.

//     function foo(a) {
//         delete a; // SyntaxError: Delete of an unqualifed identifier in strict mode.
//     }
//     delete foo; // SyntaxError: Delete of an unqualifed identifier in strict mode.
// }());

// p.318

// (function() {
//     'use strict';

//     // SyntaxError: Duplicate parameter name not allowed in this context
//     function foo(x, x) {
//         return x + x;
//     }
//     console.log(foo(1, 2));
// }());

// (function () {
//     'use strict';

//     // SyntaxError: Strict mode ode may not include a with statement
//     with({ x : 1 }) {
//         console.log(x);
//     }
// }());

// // p.319

// (function () {
//     'use strict';

//     function foo() {
//         console.log(this);
//     }
//     foo();

//     new foo();
// }());

// p.324

// // 1. 식별자 str은 문자열을 값으로 가지고 있다.
// const str = 'hello';

// // 2. 식별자 str은 암묵적으로 생성된 래퍼 객체를 기리킨다.
// // 식별자 str의 값 'hello'는 래퍼 객체의 [[string data]] 내부 슬롯에 할당된다.
// // 래퍼 객체에 name 프로퍼티가 동적 추가된다.
// str.name = 'Lee';

// // 3. 식별자 str은 다시 원래의 문자열, 즉 래퍼 객체의 [[StringData]] 내부 슬롯에 할당된 원시값을 갖는다.
// // 이때 2. 에서 생성된 래퍼 객체는 아무도 참조하지 않는 상태이므로 가비지 컬렉션의 대상이 된다.

// // 4. 식별자 str은 새롭게 암묵적으로 생성된[2. 에서 생성된 래퍼 객체와는 다른) 래퍼 객체를 가리킨다.
// // 새롭게 생성된 래퍼 객체에는 name 프로퍼티가 존재하지 않는다.
// console.log(str.name); // undefined

// // 5. 식별자 str은 다시 원래의 문자열, 즉 래퍼 객체의 [[StringData]] 내부 슬롯에 할당된 원시값을 갖는다.
// // 이때 4. 에서 생성된 래퍼 객체는 아무도 참조하지 않는 상태이므로 가비지 컬렉션의 대상이 된다.
// console.log(typeof str, str); // string Hello

// p.329

// // 표현식인 문
// eval('1 + 2;');
// // 표현식이 아닌 문
// eval('var x = 5;'); // -> undefined

// // eval 함수에 의해 런타임에 변수 선언문이 실행되어 x 변수가 선언되었다.
// console.log(x); // 5

// // 객체 리터럴은 반드시 괄호로 둘러싼다.
// const o = eval('({ a: 1 })');
// console.log(o);

// // 함수 리터럴은 반드시 괄호로 둘러싼다.
// const f = eval('(function () { return 1;})');
// console.log(f());

// p.339
// var x = 10; // 전역 변수

// function foo() {
//     // 선언하지 않은 식별자에 값을 할당
//     y = 20; // window.y = 20;
// }
// foo();

// // 선언하지 않은 식별자 y를 전역에서 참조할 수 있다.
// console.log(x + y); // 30

// p.345
// // this는 어디서든지 참조 가능하다.
// // 전역에서 this는 전역 객체 window를 가리킨다.
// console.log(this);

// function square(number) {
//     // 일반 함수 내부에서 this는 전역 객체 window를 가리킨다.
//     console.log(this);
//     return number * number;
// }
// square(2);
// new square(2);

// const person = {
//     name: 'Lee',
//     getName() {
//         // 메서드 내부에서 this는 메서드를 호출한 객체를 가리킨다.
//         console.log(this);
//         return this.name;
//     }
// };
// console.log(person.getName());

// function Person(name) {
//     this.name = name;
//     // 생성자 함수 내부에서 this는 생성자 함수가 생성할 인스턴스를 가리킨다.
//     console.log(this);
// }

// const me = new Person('Lee');

// p.351

// const person = {
//     name: 'Lee',
//     getname() {
//         // 메서드 내부의 this는 메서드를 호출한 객체에 바인딩된다.
//         return this.name;
//     }
// };

// // 메서드 getName을 호출한 객체는 person이다.
// console.log(person.getname()); // Lee

// const anotherPerson = {
//     name: 'Kim'
// };
// // getName 메서드를 anotherPerson 객체의 메서드로 할당
// anotherPerson.getName = person.getName;

// // getName 메서드를 호출한 객체는 anotherPerson이다.
// console.log(anotherPerson.getName());

// // getName 메서드를 변수에 할당
// const getName = person.getName;

// // getName 메서드를 일반 함수로 호출
// console.log(getName()); // ''
// // 일반 함수로 호출된 getName 함수 내부의 this.name은 브라우저 환경에서 window.name과 같다.

// p.402
// // 카운트 상태 변경 함수
// const increase = (function () {
//     // 카운트 상태 변수
//     let num = 0;

//     // 클로저
//     return function () {
//         // 카운트 상태를 1만큼 증가시킨다.
//         return ++num;
//     }
// }());

// console.log(increase()); // 1
// console.log(increase()); // 2
// console.log(increase()); // 3
// function makeUser() {
//     return {
//         name: "John",
//         ref: this
//     };
// };

// let user = makeUser();

// console.log(user.ref); 

// p. 429
// class Person {
//     constructor(name) {
//         this.name = name;
//     }

//     sayHi() {
//         console.log(`Hi! My name is ${this.name}`);
//     }
// }

// const me = new Person('Lee');
// me.sayHi();

// p. 431
// class Person {
//     constructor(name) {
//         this.name = name;
//     }

//     static sayHi() {
//         console.log('Hi!');
//     }
// }

// Person.sayHi(); // Hi!

// p. 435
// class Person {
//     constructor(name) {
//         // 1. 암묵적으로 인스턴스가 생성되고 this에 바인딩된다.
//         console.log(this); // person {}
//         console.log(Object.getPrototypeOf(this) === Person.prototype); // true

//         // 2. this에 바인딩되어 있는 인스턴스를 초기화한다.
//         this.name = name;

//         // 3. 완성된 인스턴스가 바인딩된 this가 암묵적으로 반환된다.
//     }
// }

// p. 436
// class Person {
//     constructor(name) {
//         this.name = name;
//     }
// }

// const me = new Person('Lee');
// console.log(me); // Person {name: "Lee"}

// p. 438
// class Person {
//     constructor(firstname, lastName) {
//         this.firstName = firstName;
//         this.lastName = lastName;
//     }

//     // fullName은 접근자 함수로 구성된 접근자 프로퍼티다.
//     // getter 함수
//     get fullName() {
//         return `${this.firstName} ${this.lastName}`;
//     }

//     // setter 함수
//     set fullName(name) {
//         [this.firstName, this.lastName] = name.split(' ');
//     }
// }

// const me = new Person('Ungmo', 'Lee');

// // 데이터 프로퍼티를 통한 프로퍼티 값의 참조.
// console.log(`${me.firstName} ${me.lastName}`) // Ungmo Lee

// // 접근자 프로퍼티를 통한 프로퍼티 값의 저장
// // 접근자 프로퍼티 fullName에 값을 저장하면 setter 함수가 호출된다.
// me.fullName = 'Heegun Lee';
// console.log(me); // {firstName: "Heegun", lastName: "Lee"}

// // 접근자 프로퍼티를 통한 프로퍼티 값의 참조
// // 접근자 프로퍼티 fullName에 접근하면 getter 함수가 호출된다.
// console.log(me.fullName); // Heegun Lee

// // fullName은 접근자 프로퍼티다.
// // 접근자 프로퍼티는 get, set, enumerable, configurable 프로퍼티 어트리뷰트를 갖는다.
// console.log(Object.getOwnPropertyDescriptor(Person.prototype, 'fullName'));
// // {get: f, set: f, enumerable: false, configurable: true}

// p. 441
class Person {
    // 클래스 필드 정으
    name = 'Lee';
}

const me = new Person();
console.log(me); // Person {name: "Lee"}