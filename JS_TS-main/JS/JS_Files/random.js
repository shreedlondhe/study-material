
let i = '2';
let j = 5;
let k = i * j;
let l = i + j;
console.log(k);//10
console.log(l);//25
console.log(l/k);//2.5

console.log('======================================================================');

let user = {
    name: 'Tom',
    age: 30,
    city: 'LA',
    isActive: true
};

for(let l in user){
    console.log(`${l}: ${user[l]}`);
};
/*
name: Tom
age: 30
city: LA
isActive: true
*/
