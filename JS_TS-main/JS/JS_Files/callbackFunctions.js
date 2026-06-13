//callback function: is a function passed as an arguement to another function.

let sayHi = function(){
    console.log('Hiiiiiii.......');
}

let sayHello = function(callback){
    callback();
}

sayHello(sayHi);//Hiiiiiii.......

console.log('======================================================================');
//1.
let addition = (a, b) => a + b;
let doAddition = function(callback){
    return callback(10, 20);
}
console.log(doAddition(addition));

console.log('======================================================================');

//2.
let add = (a, b) => a + b;
let sub = (a, b) => a - b;
let mul = (a, b) => a * b;
let div = (a, b) => a / b;

function calculator (a, b, callback){
    return callback(a, b);
};
console.log(calculator(10, 20, add));//30
let addFunction = calculator(20, 20, add);
console.log(addFunction);//40

console.log('======================================================================');

//3.
function initDriver(browserName){
    console.log('Browser name: ', browserName);

    switch (browserName.trim().toLowerCase()) {
        case 'chrome':
            console.log('Launch chrome');
            return true;
        case 'edge':
            console.log('Launch edge');
            return true;
        case 'firefox':
            console.log('Launch firefox');
            return true;
        default:
            console.log('Please pass the right browser.');
            return false;
    }
}

function enterUrl(browserName, url, callback){
    if(callback(browserName)){
        console.log('Navigate to: ', url);
    }
}

enterUrl('chrome', 'https://www.google.com', initDriver);

console.log('======================================================================');

//4.
function myCalci(a, b, callback){
    return callback(a, b);
};

console.log(myCalci(10, 20, (a, b)=>a+b));//30
let s1 = myCalci(30, 20, (a, b)=>a+b);
console.log(s1);//50

console.log('======================================================================');

//5.
function launchTheBrowser(browserName, callback){
    return callback(browserName);
};
launchTheBrowser('chrome', 
    (browserName)=>{
        console.log('Browser name: ', browserName);
        switch (browserName.trim().toLowerCase()) {
            case 'chrome':
                console.log('Launch chrome');
                return true;
            case 'edge':
                console.log('Launch edge');
                return true;
            case 'firefox':
                console.log('Launch firefox');
                return true;
            default:
                console.log('Please pass the right browser.');
                return false;
        }
    }
);

console.log('======================================================================');

//6.
let num = [1, 2, 3, 4, 5];
num.forEach(e => console.log(e));
/*
1
2
3
4
5
*/

console.log('======================================================================');

//7.
num.forEach((n) => {
    console.log(n+1);
});
/*
2
3
4
5
6
*/

console.log('======================================================================');

//8.
let n = num.filter(e => e%2==0);
console.log(n);//[ 2, 4 ]

console.log('======================================================================');

//9.
let mappedNums = num.map(e => e * 2);
console.log(mappedNums);//[ 2, 4, 6, 8, 10 ]

console.log('======================================================================');

//10.
function myCalc(a, b, callback){
    return callback(a, b);
};

let s3 = myCalc(100, 400, function(a, b){
    return a + b;
});
console.log(s3);//500

console.log('======================================================================');

//1.
function greet1(name){
    console.log(`Hi, ${name}`);
}

function processUser1(username, callback){
    console.log('Processing...');
    callback(username);
}

processUser1('Sachin', greet1);
/*
Processing...
Hi, Sachin
*/

//2.
//callback with anonymous function:
let greet2 = function(name){
    console.log('Hi, ', name);
}

function processUser2(name, callback){
    console.log('Processing..');
    callback(name);
}

processUser2('Sachin', greet2);
/*
Processing..
Hi,  Sachin
*/

//3.
//callback with arrow function:
let u = (name) => {
    console.log('Hi, ', name);
};

function processUser3(username, callback){
    console.log('Processing...');
    callback(username);
}

processUser3('Sachin', u);

//4.
//callback with setTimeout
function processUser4(callback){
    setTimeout((username)=>{
        console.log('Processing...', username);
        callback(username);
    }, 5000, 'Sachin');
}

processUser4(greet1);
/*
Processing... Sachin
Hi, Sachin
*/

//5.
//callback with setTimeout
console.log('1. Start');
setTimeout(() => {
    console.log('3. done');
}, 2000);
console.log('2. End');
/*
1. Start
2. End
3. done
*/


//After execution:
/*
o/p for both setTimeout():
1. Start
2. End
3. done
Processing... Sachin
Hi, Sachin
*/
