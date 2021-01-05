// 1. var, let, const

// var: 변수 유효범위 구분 x
// let: 변수 유효범위 구분 o, (ECMA6에서 나옴)var 개선
// const: 상수, 값 변경시 에러

let x;
x = 6;
const constVariable = 10;
let globalVariable = 5;
{
    let localVariable = 5;
    var y = 5;
    console.log("localVariable -> ", localVariable);
    console.log("globalVariable -> ", globalVariable);
    console.log("constVariable -> ", constVariable);
    console.log("let x -> ", x);
    console.log("var y -> ", y);
}
//constVariable = 100;  // 에러 발생
// console.log("localVariable ", localVariable);  // 에러 발생
console.log("globalVariable -> ", globalVariable);
console.log("constVariable -> ", constVariable);
console.log("let x -> ", x);
console.log("var y -> ", y);

document.getElementById("data").innerHTML = "<h3> variable x = " + x + "</h3>";

//2. DataType - Primitive(int, float, string, boolean), Reference(Class, Array)
let intV = 10;
let floatV = 10.5;
let stringV = "10";
let booleanV = true;
console.log("data type ", intV, floatV, stringV, booleanV)
