
/*
    Best SOLUTION TO CALLBACK HELL:
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

async function taskSequence(){
    await tasc1();
    await tasc2();
    await tasc3();
    await tasc4();
    await tasc5();
    console.log('DONE');
};
taskSequence();
