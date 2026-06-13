
//Promise: is used to handle asynchronous operations (asynchronous: operations take time)

/*
E.g.
1. API calls
2. File reading
3. DB Query
4. AJAX: The Asynchronous JavaScript and XML, usually referred as Ajax is a set of web development techniques 
    that uses various web technologies on the client-side to create asynchronous web applications.
5. Timers: e.g. setTimeout
*/

/*
Many times the callback creates problems like callback hell. To resolve the issues with callbacks, JS has introduced promises to handle
async operations.

A Promise is an object that represents: A value that will be available in the future.

Promise States --> A Promise has 3 states:
    - Pending → Initial state
    - Resolved (Fulfilled) → Success
    - Rejected → Failure

Why Promises Matter (Automation Testing  with Cypress / Playwright):

    With automation tools:
    - API calls → async
    - UI actions → async
    - Waiting for elements → async

    Promises help:
    - Control execution order
    - Avoid flaky tests
    - Handle delays properly
*/



/*
var Promise: PromiseConstructor
new <any>(executor: (resolve: (value: any) => void, reject: (reason?: any) => void) => void) => Promise<any>
Creates a new Promise.

@param executor
A callback used to initialize the promise. This callback is passed two arguments: a resolve callback used to resolve the promise with 
a value or the result of another promise, and a reject callback used to reject the promise with a provided reason or error.
*/
let myPromise = new Promise((resolve, rejected) => {
    let success = true;
    if(success){
        resolve('Task completed --> 200 OK');
    } else{
        rejected('Task failed --> 500 ERROR');
    }
});

myPromise
    .then((result) => {
        console.log(result);
    })
    .catch((error)=>{
        console.log(error);
    })

/*
true: Task completed --> 200 OK
false: Task failed --> 500 ERROR
*/

console.log('======================================================================');


//Example: A real async operation: with setTimeout

//1.
let dataPromise = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        console.log('Resolve the promise');
        resolve('Data is received from the server');
    }, 3000);
});

dataPromise
    .then((result)=>{
        console.log(result);
    })
    .catch((error)=>{
        console.log(error);
    });

console.log('======================================================================');

//2.
let dataPromise2 = new Promise((resolve, reject)=>{
    setTimeout((flag)=>{
        if(flag){
            console.log('Resolve the promise..');
            resolve('Data is received from the server');
        } else{
            console.log('Reject the promise..');
            reject('Data is not received');
        }
        
    }, 5000, false);
});

dataPromise2
    .then((result)=>{
        console.log(result);
    })
    .catch((error)=>{
        console.log(error);
    });

console.log('======================================================================');

//3.
function fetchUser(){
    return new Promise((resolve, reject)=>{
        setTimeout((flag)=>{
            if(flag){
            let user = {
                name: 'Priya',
                role: 'QA'
            };
            resolve(user);
            } else{
                reject('User is not found: 404 NOT FOUND');
            }
        }, 7000, true);
    });
};

fetchUser()
    .then((result)=>{
        console.log(result);
    })
    .catch((error)=>{
        console.log(error);
    })
    .finally(()=>{
        console.log('Disconnect with the database..');
    })
/*
o/p --> if resolved: 
{ name: 'Priya', role: 'QA' }
 Disconnect with the database..
*/


console.log('======================================================================');


//Promise chaining:

let p1 = new Promise((resolve, reject)=>{
    resolve(5);
});

p1
    .then(n => n*2)
    .then(n => n*3)
    .then(result => console.log(result))

/*
o/p --> if resolved: 
30
*/
