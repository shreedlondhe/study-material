//An object can have all data types:
let o = {
    o1: [],
    o2: class c{
        companyName;

        constructor(companyName){
            this.companyName = companyName;
        };

        m1(){
            console.log('This is m1');
        };
    },
    o3: function f(){
        return true;
    },
    o4: obj = {
        obj1: 1,
        obj2: 'Hello'
    },
    o5: p1 = new Promise((resolve)=>{
        resolve('Promise resolved');
    }),
    o6: s1 = setTimeout(()=>{
        let data = {
            name: 'Sachin',
            age: 37
        };
        console.log(data);
    }, 1000),
    o7: f = (a) => console.log(a)
};
