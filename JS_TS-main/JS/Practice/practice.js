
const s1 = "Sachinaaa";
console.log();
console.log(s1.length);

console.log(s1.indexOf('c'));

const secOcc = s1.indexOf('a')+1;
console.log(s1.indexOf('a', s1.indexOf('a')+1));
console.log(s1.indexOf('a', s1.indexOf('a', s1.indexOf('a', s1.indexOf('a')+1)+1)+1));

console.log(s1.lastIndexOf('Sachin'));
console.log(s1.lastIndexOf('a'));

console.log(s1.includes('Sachin'));

console.log(s1.startsWith('S'));

console.log(s1.endsWith('Sachinaaa'));

console.log(s1.slice(0, 2));

let s6 = '7';
let r3 = s6.padStart(3, '0');
console.log(r3);//007

console.log(s1.charAt(0));
console.log(s1.at(0));

console.log(s1[1]);

let num = [];
num.push(1, 2, 3, 4, 5);
console.log(num);

let slicedS1 = s1.slice(2, s1.length-1)
console.log(slicedS1);
console.log(s1);



let nums = [1, 2, 3, 4, 5];

nums.map((num)=>{

});


((a) => console.log(a + 4))(5);


let s = 'Sachin Ade';

