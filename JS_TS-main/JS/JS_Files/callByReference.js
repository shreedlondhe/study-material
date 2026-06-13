
let user = {
    name: 'Pratik',
    age: 30,
    city: 'Pune'
}

/**
 * 
 * @param {object} object1 
 */
function printUserData1(object1){
    console.log(object1);
}
printUserData1(user);//{ name: 'Pratik', age: 30, city: 'Pune' }

console.log('======================================================================');

function printUserData2(object2){
    object2.age = 40;
    object2.zipcode = 431131;
    console.log(object2);
}
printUserData2(user);//{ name: 'Pratik', age: 40, city: 'Pune', zipcode: 431131 }
console.log(user.age);//40
console.log(user);//{ name: 'Pratik', age: 40, city: 'Pune', zipcode: 431131 }
