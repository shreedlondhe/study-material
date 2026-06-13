
//callback hell:
function task1(callback){
    console.log('Turn on the Gas..');
    callback();
};

function task2(callback){
    console.log('Put a pot on the Gas with some water.');
    callback();
};

function task3(callback){
    console.log('Wait until water boils.');
    callback();
};

function task4(callback){
    console.log('Put eggs inside the pot with boiled water.');
    callback();
};

function task5(callback){
    console.log('Wait for 20 minutes to prepare the boiled egg');
    callback();
};


task1(()=>{
    task2(()=>{
        task3(()=>{
            task4(()=>{
                task5(()=>{
                    console.log('DONE');
                })
            })
        })
    });
});

/*
Turn on the Gas..
Put a pot on the Gas with some water.
Wait until water boils.
Put eggs inside the pot with boiled water.
Wait for 20 minutes to prepare the boiled egg
DONE
*/


console.log('=======================================================================================');


/*
    SOLUTION TO CALLBACK HELL:
*/

//callback hell solution:
function tasc1(){
    return new Promise((resolve)=>{
        console.log('Turn on the Gas..')
        resolve();
    });
};

function tasc2(){
    return new Promise((resolve)=>{
        console.log('Put a pot on the Gas with some water.');
        resolve();
    });
};

function tasc3(){
    return new Promise((resolve)=>{
        console.log('Wait until water boils.');
        resolve();
    });
};

function tasc4(){
    return new Promise((resolve)=>{
        console.log('Put eggs inside the pot with boiled water.');
        resolve();
    });
};

function tasc5(){
    return new Promise((resolve)=>{
        console.log('Wait for 20 minutes to prepare the boiled egg');
        resolve();
    });
};

tasc1()
    .then(() => tasc2())
    .then(() => tasc3())
    .then(() => tasc4())
    .then(() => tasc5())
    .then(()=>console.log('DONE'));

/*
Turn on the Gas..
Put a pot on the Gas with some water.
Wait until water boils.
Put eggs inside the pot with boiled water.
Wait for 20 minutes to prepare the boiled egg
DONE
*/
