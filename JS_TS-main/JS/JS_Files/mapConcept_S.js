
//Map:

/*
set():
    (method) Map<any, any>.set(key: any, value: any): Map<any, any>
    Adds a new element with a specified key and value to the Map. 
    If an element with the same key already exists, the element will be updated.
*/
let sqr = new Map();
sqr.set(1, 1);
sqr.set(2, 4);
sqr.set(3, 9);
sqr.set(4, 16);
sqr.set(5, 25);
console.log(sqr);
console.log(typeof sqr);//object
/*
Map(5) { 1 => 1, 2 => 4, 3 => 9, 4 => 16, 5 => 25 }
*/

console.log('======================================================================');

let myArr = [['name', 'Sachin'], ['age', 37], ['city', 'Pune'], ['pin', 123456], ['isActive', true]];
let myInfo = new Map(myArr);
console.log(myInfo);
/*
Map(5) {
  'name' => 'Sachin',
  'age' => 37,
  'city' => 'Pune',
  'pin' => 123456,
  'isActive' => true
}
*/

console.log('======================================================================');

//Update existing value:
myInfo.set('pin', 122334);
console.log(myInfo);
/*
Map(5) {
  'name' => 'Sachin',
  'age' => 37,
  'city' => 'Pune',
  'pin' => 122334,
  'isActive' => true
}
*/

console.log('======================================================================');

/*
get():
    (method) Map<any, any>.get(key: any): any
    Returns a specified element from the Map object. If the value that is associated to the provided key is an object, then you will get 
    a reference to that object and any change made to that object will effectively modify it inside the Map.

    @returns — Returns the element associated with the specified key. If no element is associated with the specified key, 
    undefined is returned.
*/
let myAge = myInfo.get('Age');
console.log(myAge);//37

console.log('======================================================================');

/*
size:
    (property) Map<any, any>.size: number
    @returns — the number of elements in the Map.
*/
let myInfoSize = myInfo.size;
console.log(myInfoSize);//5

console.log('======================================================================');

/*
delete(): 
    (method) Map<any, any>.delete(key: any): boolean
    @returns — true if an element in the Map existed and has been removed, or false if the element does not exist.
*/
myInfo.set('Hobby', 'Singing songs');
console.log(myInfo.size);//6
myInfo.delete('pin');
console.log(myInfo);
/*
Map(5) {
  'name' => 'Sachin',
  'age' => 37,
  'city' => 'Pune',
  'isActive' => true,
  'Hobby' => 'Singing songs'
}
*/

console.log('======================================================================');

/*
has():
    (method) Map<any, any>.has(key: any): boolean
    @returns — boolean indicating whether an element with the specified key exists or not.
*/
let flg1 = myInfo.has('isActive');
console.log(flg1);//true

console.log('======================================================================');

/*
forEach():
    (method) Map<any, any>.forEach(callbackfn: (value: any, key: any, map: Map<any, any>) => void, thisArg?: any): void
    Executes a provided function once per each key/value pair in the Map, in insertion order.
*/
myInfo.forEach((e)=>console.log(e));
/*
Sachin
37
Pune
true
Singing songs
*/

console.log('======================================================================');

for(const e of myInfo.entries()){
    console.log(e);
};
/*
[ 'name', 'Sachin' ]
[ 'age', 37 ]
[ 'city', 'Pune' ]
[ 'isActive', true ]
[ 'Hobby', 'Singing songs' ]
*/

console.log('======================================================================');

/*
keys():
    (method) Map<any, any>.keys(): MapIterator<any>
    Returns an iterable of keys in the map
*/
for(const key of myInfo.keys()){
    console.log(key);
};
/*
name
age
city
isActive
Hobby
*/

console.log('======================================================================');

/*
values():
    (method) Map<any, any>.values(): MapIterator<any>
    Returns an iterable of values in the map
*/
for(const value of myInfo.values()){
    console.log(value);
};
/*
Sachin
37
Pune
true
Singing songs
*/
