
function startMachine(){
    return new Promise((resolve, reject)=>{
        setTimeout((flag)=>{
            if(flag){
                resolve('Machine started..');
            } else{
                reject('Machine failed to start..');
            }
        }, 5000, true);
    });
};

function grindBeans(){
    return new Promise((resolve, reject)=>{
        setTimeout((flag)=>{
            if(flag){
                resolve('Grind the beans..');
            } else{
                reject('Cannot grind the beans..');
            }
        }, 3000, true);
    });
};

function boilWater(){
    return new Promise((resolve, reject)=>{
        setTimeout((flag)=>{
            if(flag){
                resolve('Water is boiled..');
            } else{
                reject('Cannot boil the water..');
            }
        }, 4000, true);
    });
};

function brewCoffee(){
    return new Promise((resolve, reject)=>{
        setTimeout((flag)=>{
            if(flag){
                resolve('Brew the coffee..');
            } else{
                reject('Cannot brew the coffee..');
            }
        }, 3000, true);
    });
}

function pourCoffee(){
    return new Promise((resolve, reject)=>{
        setTimeout((flag)=>{
            if(flag){
                resolve('Pour the coffee into the cup..');
            } else{
                reject('Cannot pour the coffee into the cup..');
            }
        }, 2000, true);
    });
}

function stopMachine(){
    return new Promise((resolve, reject)=>{
        setTimeout((flag)=>{
            if(flag){
                resolve('Stop the machine..');
            } else{
                reject('Cannot stop the machine..');
            }
        }, 4000, true);
    });
}


startMachine()
    .then((result) => {
        console.log(result);
        return grindBeans();
    })
    .then((result)=>{
        console.log(result);
        return boilWater();
    })
    .then((result)=>{
        console.log(result);
        return brewCoffee();
    })
    .then((result)=>{
        console.log(result);
        return pourCoffee();
    })
    .then((result)=>{
        console.log(result);
        return stopMachine();
    })
    .then((result)=>{
        console.log(result);
        console.log('Enjoy the coffee. Thank you..');
    })
    .finally(()=>{
        console.log('Go back to your desk.');
    });
