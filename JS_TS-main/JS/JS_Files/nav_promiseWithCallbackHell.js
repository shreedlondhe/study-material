
function startMachine(){
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            console.log('Start the machine..');
            resolve();
        }, 5000);
    });
};

function grindBeans(){
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            console.log('Grind the beans..');
            resolve();
        }, 3000);
    });
};

function boilWater(){
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            console.log('Boil the water..');
            resolve();
        }, 4000);
    });
};

function brewCoffee(){
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            console.log('Brew the coffee..');
            resolve();
        }, 3000);
    });
};

function pourCoffee(){
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            console.log('Pour the coffee into the cup..');
            resolve();
        }, 2000);
    });
};

function stopMachine(){
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            console.log('Stop the machine..');
            resolve();
        }, 4000);
    });
}

startMachine()
    .then(()=>grindBeans())
    .then(()=>boilWater())
    .then(()=>brewCoffee())
    .then(()=>pourCoffee())
    .then(()=>stopMachine())
    .then(()=>console.log('Enjoy the coffee.. Thank you..'))
    .finally(()=>console.log('After finishing your coffee, please go back to your desk. Thanks.'));
