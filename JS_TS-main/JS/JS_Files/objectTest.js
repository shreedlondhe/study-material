let u1 = {
    name: 'Ravi',
    age: 30,
    city: 'Mumbai'
};

console.log(u1.name);//Ravi
console.log(u1.age);//30
console.log(u1.country);//undefined

console.log('======================================================================');

let u2 = {
    name: 'Ankita',
    age: 25,
    city: 'Pune',
    country: 'India'
};

console.log(u2.name);//Ankita
console.log(u2.age);//25
console.log(u2.country);//India

console.log('======================================================================');

u1 = u2;

console.log(u1.name);//Ankita
console.log(u1.age);//25
console.log(u1.country);//India

console.log('======================================================================');

let u3 = {};
console.log(u3);//{}
u3 = u1;
console.log(u3);//{ name: 'Ankita', age: 25, city: 'Pune', country: 'India' }


console.log(u1);//{ name: 'Ankita', age: 25, city: 'Pune', country: 'India' }
let u4 = {};
u1 = u4;
console.log(u1);//{}
