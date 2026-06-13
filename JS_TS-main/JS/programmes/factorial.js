
function factorial(n) {
    if(n === 1) {
        return 1;
    }

    return n * factorial(n - 1);
}

console.log(factorial(5));



//Factorial program:
//Approach 1:
/*
    5! = (5-0) * (5-1)  * (5-2) 60 * (5-3) * (5-4);
*/
function getFactorialOfNum(num){
    let c = num;
    for(let i=1; i<num; i++){
        c = c * (num - i);
    }
    console.log(c);
}
getFactorialOfNum(4);


//Approach 2 --> Best approach:
function fact(num){
    if(num<0){
        return `The ${num} is a -ve number. Please pass a +ve number.`;
    }
    if(num == 0 || num == 1){
        return 1;
    }
    return num * fact(num - 1);
}
console.log(fact(-1));
