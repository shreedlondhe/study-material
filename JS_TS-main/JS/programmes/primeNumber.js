
/* Will not work always:

    let numArr = [1, 2, 3, 4, 5, 7, 10, 11, 18, 19, 119, 120, 221, 530, 450, 996];
    let s = [];

    for(let i=0; i<numArr.length; i++){
        if(numArr[i]==1){
            numArr.splice(i,1);
        }
        for(let j=0; j<numArr.length; j++){
            if(numArr[i]!=numArr[j] && numArr[i]%numArr[j]==0){
                s=numArr.splice(i, 1);
                i--;
                break;
            }
        };
    }
    console.log(numArr);

*/

let numArr = [1, 2, 3, 4, 5, 7, 10, 11, 18, 19, 119, 120, 221, 530, 450, 996];
let arr = [];
for(let i=0; i<numArr.length; i++){
    let primeFlag = true;
    if(numArr[i]<2){
        primeFlag = false;
    };

    for(let j=2; j<numArr[i]; j++){
        if(numArr[i]%j==0){
            primeFlag = false;
        };
    };

    if(primeFlag){
        arr.push(numArr[i]);
    };
};
console.log(arr);

