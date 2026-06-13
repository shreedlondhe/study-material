
let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

let [a, ...nums] = arr;
console.log(a);//1
console.log(nums);
/*
[
  2, 3, 4,  5, 6,
  7, 8, 9, 10
]
*/


const ar1 = [12, 23, 34, 45];
const ar2 = [112, 123, 134, 145];
const ar3 = [...ar1, ...ar2];

console.log(...ar1, ...ar2);
/*
12 23 34 45 112 123 134 145
*/
console.log(...ar1);//12 23 34 45

console.log(...ar2);//112 123 134 145

console.log(ar3);
/*
[
   12,  23,  34,  45,
  112, 123, 134, 145
]
*/


const [a1, ...a2] = ar3;
console.log(a1);//12
console.log(a2);
/*
[
   23,  34,  45, 112,
  123, 134, 145
]
*/


console.log('=======================================');

const str = 'Hello';
console.log(str);
console.log(...str);
console.log(...str.at(1));
const strArr = [...str];
console.log(strArr);
const [s1, ...s2] = strArr;
console.log(s1);
console.log(s2);


console.log('=======================================');

function add(...numbers){
    let sum = 0;
    for(let number of numbers){
        sum = sum + number;
    }
    return sum;
};

console.log(add(10, 2, 15, 25));//52
