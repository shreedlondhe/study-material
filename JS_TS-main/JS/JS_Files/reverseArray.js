//Reverse the array by using for, for..of, for..in loops
let num = [1, 2, 3, 4, 5, 6];

//1. for loop:
for(let i=num.length-1; i>=0; i--){
    console.log(num[i]);
}

console.log('======================================================================');

//1.1 for loop:
let num0 = num.reverse();
for(let i=0; i<num0.length; i++){
    console.log(num[i]);
}

console.log('======================================================================');

//2. for..of:
let num1 = [1, 2, 3, 4, 5, 6];
for(let i of num1.reverse()){
    console.log(i);
}

console.log('======================================================================');

//2.1 for..of:
let num11 = [1, 2, 3, 4, 5, 6];
let count1 = num11.length-1;
for(let i of num11){
    i=num11[count1];
    console.log(i);
    count1--;
}

console.log('======================================================================');

//2.2 for..of:
let num12 = [1, 2, 3, 4, 5, 6];
for(let i of num12){
     let count2 =  num12.length - num12.indexOf(i) - 1;
     console.log(num12[count2]);
}

console.log('======================================================================');

//3. for..in:
let num2 = [1, 2, 3, 4, 5, 6];
for(let i in num2.reverse()){
    console.log(num[i]);
}

console.log('======================================================================');

//3.1 for..in:
let num3 = [1, 2, 3, 4, 5, 6];
let count = num3.length-1;
for(let i in num3){
    i=count;
    console.log(num3[i]);
    count--;
}
