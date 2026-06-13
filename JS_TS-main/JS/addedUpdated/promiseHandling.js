
//1.
const promise = new Promise((resolve, reject)=>{
    let flag = true;
    setTimeout((flag)=>{
        resolve('processing...');
    }, 5000);
});

function aprm(){
    return promise;
};

async function myPromise(){
    console.log('Start');
    console.log(await aprm());
    console.log('End');
}

myPromise();


//2.
const resolvedPromise = new Promise((resolve, reject)=>{
    resolve('Passed...');
});
resolvedPromise.then((result)=>console.log(result));//Passed...


//3.
const rejectedPromise = new Promise((resolve, reject)=>{
    reject('Failed...');
});
rejectedPromise.catch((error)=>console.log(error))//Failed...


//4.
const resolveRejectPromise = new Promise((resolve, reject)=>{
    let flag = true;
    if(flag){
        resolve('Resolved --> Succeeded');
    } else{
        reject('Rejected --> Unsucceeded')
    };
});
resolveRejectPromise
    .then((result)=>console.log(result))
    .catch((error)=>console.log(error))
    .finally(()=>console.log('Completed testing..'))
/*
Resolved --> Succeeded
Completed testing..
*/




