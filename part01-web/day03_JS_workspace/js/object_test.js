// class: object를 생성하기 위한 template
// object: class type으로 생성된 변수
// 1. Class 선언(ECMA6 - class)

// class 클래스 이름{
//     변수;
//     메소드;
// }

class Person {
    name = "";
    age = 0;
    // name="";
    // age=0;

    constructor(name, age) {
        this.name = name;
        this.age = age;
        // this가 다른 것을 의미할 때도 있어서 변수선언을 다르게 하고
        // 아래처럼 적기도 함
        // _name=name;
        // _age=age;
    }
    print() {
        console.log(`이름: ${this.name} 나이: ${this.age}`);
    }

    // computed
    get birthYear() {
        return 2021 - this.age + 1;
    }

    // action
    set birthYear(year) {
        this.age = 2021 - year + 1;
    }
}

let p = new Person("Wansang Kim", 29);
console.log(`${p.name}님 ${p.birthYear}년 출생`);
p.age = 2000000000000
p.print();

// p.birthYear(1997)  // error 발생 - not a function - Type error
p.birthYear = 1997;
p.print();

// 2. function 객체로 선언
function Student(name, age, major) {
    this.name = name;
    this.age = age;
    this.major = major;
    this.print = function () {
        console.log(`이름: ${this.name}, 나이: ${this.age}, 전공: ${this.major}`);
    }
}

// JS 초창기 
// Student.prototype.print: function(){
//     ...
// }

let s = new Student("허성현", 26, "컴퓨터공학");
s.print();

// 3. JSON(Javascript Object Notation): 데이터 교환
let e = { name: 'Wansang', age: 28, department: '연구소', array: [1, 2, 3, 4], male: 'man' };
let array = [{ name: 'Wansang', age: 28 }, 1, [1, 2, 3, 4], 'name',]
console.log(e);
