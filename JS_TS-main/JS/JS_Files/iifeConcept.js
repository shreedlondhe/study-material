//IIFE: Immediate Invoke Function Expressions

//The function given below does not have name. This is an anonymus function.

(function () {
    console.log('Hello world..');
    console.log(10 + 10);
})();
/*
Hello world..
20
*/

console.log('======================================================================');

let t1 = (function () {
    console.log('Hello world..');
    console.log(10 + 10);
})();

//t1();//TypeError: t1 is not a function
t1;//Valid
/*
Hello world..
20
*/

console.log('======================================================================');

(function () {
    console.log('Hiiiiii........');
})();
//Hiiiiii........

console.log('======================================================================');

(function (browserName){
    console.log('launch browser: ', browserName);
})('chrome');
//launch browser:  chrome

console.log('======================================================================');

let t2 = (function () {
    console.log('Hello world..');
    console.log(10 + 10);
});
t2();
/*
Hello world..
20
*/
