
let name = "Sachin";
function show() {
    console.log(name);
}
show();

//======================================================

let age;//Global Scope
function test() {
    age = 25;//function scope
    return age;
}
console.log(age);//undefined

//======================================================

let a = 50;//Global Scope
function A(){
    console.log(a);
};
A();//50

//======================================================

const nums = [10, 20, 30];
console.log(Math.max(...nums));//30
console.log(Math.min(...nums));//10

//======================================================

const user = {
  name: "Sachin",
  address: {
    city: "Pune"
  }
};

const copiedUser = {...user};

console.log(copiedUser);
/*
{ name: 'Sachin', address: { city: 'Pune' } }
*/

copiedUser.address.city = "Mumbai";

console.log(user.address.city);

console.log(copiedUser);
/*
{ name: 'Sachin', address: { city: 'Mumbai' } }
*/

//======================================================

function greet1(name){
  console.log('Hello,', name);
};

function callSomeone(name, callback){
  callback(name);
};

callSomeone('Sachin', greet1);//Hello, Sachin

//======================================================

let f = (function(){
  console.log('qwerty');
})();

f;

//======================================================


