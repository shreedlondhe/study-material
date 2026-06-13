//JS object --> JSON: Serialization (marshelling)
//JSON --> JS object: De-serialization (unmarshelling)

//API automation:
//Post call: URL, JSON
//User Object in JS --> JSON string (JSON is not Object, its a string)
//JSON: JavaScript Object Notation

//API response (JSON) --> JS object


let user = {
    name: 'Tom',
    age: 30,
    city: 'LA',
    isActive: true
};


/*
stringify():
    (method) JSON.stringify(value: any, replacer?: ((this: any, key: string, value: any) => any) | undefined, space?: string | number | undefined): string (+1 overload)
    Converts a JavaScript value to a JavaScript Object Notation (JSON) string.

    @param value — A JavaScript value, usually an object or array, to be converted.

    @param replacer — A function that transforms the results.

    @param space — Adds indentation, white space, and line break characters to the return-value JSON text to make it easier to read.

    @throws — {TypeError} If a circular reference or a BigInt value is found.
*/


/*
IMPORTANT_1:
    JS object to JSON conversion:
*/
let userJsonStr = JSON.stringify(user);
console.log(userJsonStr);//JSON string
/*
{"name":"Tom","age":30,"city":"LA","isActive":true}
*/
console.log(user);//JS object
/*
{ name: 'Tom', age: 30, city: 'LA', isActive: true }
*/

console.log(typeof userJsonStr);//string
console.log(typeof user);//object

//log in the json format:
let newUser = {
    name: 'Tom',
    age: 30,
    city: 'LA',
    isActive: true
};

let newUserJsonStr = JSON.stringify(newUser, null, 2);
console.log(newUserJsonStr);
/*
{
  "name": "Tom",
  "age": 30,
  "city": "LA",
  "isActive": true
}
*/

console.log('======================================================================');


/*
parse():
    (method) JSON.parse(text: string, reviver?: ((this: any, key: string, value: any) => any) | undefined): any
    Converts a JavaScript Object Notation (JSON) string into an object.

    @param text — A valid JSON string.

    @param reviver
    A function that transforms the results. This function is called for each member of the object. If a member contains nested objects, the nested objects are transformed before the parent object is.

    @throws — {SyntaxError} If text is not valid JSON.
*/

/*
IMPORTANT_2:
    JSON to JS object conversion:
*/

let newUserObject = JSON.parse(newUserJsonStr);
console.log(typeof newUserObject);//object
console.log(newUserObject);//{ name: 'Tom', age: 30, city: 'LA', isActive: true }

//Both objects are different. However, the key and values are same.
//object 
console.log(newUserObject === newUser);//false
console.log(newUserObject.name === newUser.name);//true


//Serialization and De-serialization example:
let customer = {
        name: 'Ravi',
        age: 30,
        city: 'Pune',
        isActive: true,
        address: {
            flat: 101,
            zip: 432121,
            lat: 10.34,
            long: 11.22
        },
        devices: ['iphone', 'mouse', 'keyboard']
};

//Serialization: JS object to JSON string
let customerJsonStr = JSON.stringify(customer, null, 2);
console.log(customerJsonStr);
/*
{
  "name": "Ravi",
  "age": 30,
  "city": "Pune",
  "isActive": true,
  "address": {
    "flat": 101,
    "zip": 432121,
    "lat": 10.34,
    "long": 11.22
  },
  "devices": [
    "iphone",
    "mouse",
    "keyboard"
  ]
}
*/
console.log(typeof customerJsonStr);//string


//De-serialization: JSON string to JS object
let customerObj = JSON.parse(customerJsonStr);
console.log(customerObj);
/*
{
  name: 'Ravi',
  age: 30,
  city: 'Pune',
  isActive: true,
  address: { flat: 101, zip: 432121, lat: 10.34, long: 11.22 },
  devices: [ 'iphone', 'mouse', 'keyboard' ]
}
*/
console.log(typeof customerObj);//object

//Assertion:
if(customer.devices.length === customerObj.devices.length){
    console.log('PASSED');
} else{
    console.log('FAILED');
}

