//null and undefined handling:
let obj1 = {
    name: 'Tom',
    age: 20
};
obj1 = null;
console.log(obj1);//null

let obj2 = {
    name: 'Tom',
    age: 20
};
obj2 = undefined;
console.log(obj2);//undefined


//console.log(obj1.name);//TypeError: Cannot read properties of null (reading 'name')

//I can reach below line only and only if I comment above line.
//console.log(obj2.name);//TypeError: Cannot read properties of undefined (reading 'name')

//To overcome this without using error handling:
console.log(obj1?.name);//undefined
console.log(obj2?.name);//undefined
