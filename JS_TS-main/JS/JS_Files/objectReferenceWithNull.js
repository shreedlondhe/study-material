//null reference is not allowed in JS:

let user = {
    name: 'Tom',
    age: 30,
    city: 'LA',
    isActive: true
};

console.log(user.name);//Tom

user = null;
console.log(user.name);//--> user.name = null.name;
//TypeError: Cannot read properties of null (reading 'name')


//
let u1 = {
    name: 'Tom',
    age: 30,
    city: 'LA',
    isActive: true
};

let u2 = {
    name: 'Naveen',
    age: 30,
    city: 'Pune',
    isActive: true
};

u1 = u2;

//GC will destroy the first object which was earlier pointed by u1.
//Currently u1 and u2 both point 2nd object i.e. the name with 'Naveen' object.
