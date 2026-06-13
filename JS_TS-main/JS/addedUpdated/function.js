
//1.
function sayHello(){
    return "Hello";
};
console.log(sayHello());

//2.
let text = sayHello;
console.log(text);//[Function: sayHello]
console.log(text());//Hello

console.log('================================');

//3.
let txt = function myText(){
    return "My text";
};
//console.log(myText());//--> ReferenceError: myText is not defined
//myText();//--> ReferenceError: myText is not defined
console.log(txt);//[Function: myText]
console.log(txt());//My text

console.log('================================');

//4.
function hello(name){
    console.log('Hello', name);
};
const greet = hello;
greet('Prince');


//5. Default Parameter Values
function f1(a, b = 10){
    return a+b;
};

console.log(f1(20));//30
console.log(f1(30, 40));//70


//6.
function f2(){
    return "Hello world!!!";
};
//6.1
const res1 = f2;
console.log(typeof(res1));//function
console.log(res1());//Hello world!!!
//6.2
const res2 = f2();
console.log(typeof(res2));//string
console.log(res2);//Hello world!!!

console.log('================================');

//7.
function f3(){
    console.log("Sachin Ade");
};
f3();//Sachin Ade
console.log(f3());
/*
Sachin Ade
undefined
*/
//7.1
const res3 = f3;
console.log(typeof(res3));//function
console.log(res3());//Sachin Ade
/*
Sachin Ade
undefined
*/
res3();//Sachin Ade
console.log('================================');
//7.2
const res4 = f3();//--> this line first executes f3() and then assign value to the res4 variable, and the res4 become undefined
console.log(typeof(res4));//undefined
console.log(res4);//undefined
//res4();//TypeError: res4 is not a function


function f4(){
    console.log('Hello...');
    return "greetings";
};
