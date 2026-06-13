let num = [
    [1, 2, 3],
    [10, 20, 30],
    [100, 200, 300]
];
console.log(num[0][0]);//1
console.log(num[1][1]);//20
console.log(num[2][2]);//300

console.log('======================================================================');

//for loop:
//1.
for(let r=0; r<num.length; r++){
    for(let c=0; c<num.length; c++){
        console.log(num[r][c]);
    }
}

console.log('======================================================================');

//2.
for(let r=0; r<num.length; r++){
    for(let c=0; c<num.length; c++){
        console.log(num[c][r]);
    }
}

console.log('======================================================================');

//for loop:
//1.
for(let r=0; r<num.length; r++){
    for(let c=0; c<num.length; c++){
        console.log(num[r][c]);
    }
    console.log();
}

console.log('======================================================================');

//2.
for(let r=0; r<num.length; r++){
    for(let c=0; c<num.length; c++){
        console.log(num[c][r]);
    }
    console.log();
}

console.log('======================================================================');

//for loop:
//1.
for(let r=0; r<num.length; r++){
    for(let c=0; c<num.length; c++){
        process.stdout.write(`${num[r][c]} `);
    }
    process.stdout.write('\n');
}

console.log('======================================================================');

for(let r=0; r<num.length; r++){
    for(let c=0; c<num.length; c++){
        process.stdout.write(`${num[c][r]} `);
    }
    process.stdout.write('\n');
}

console.log('======================================================================');

for(let r=0; r<num.length; r++){
    for(let c=0; c<num[r].length; c++){
        console.log(num[r][c]);
    }
}

console.log('======================================================================');

for(let r=0; r<num.length; r++){
    for(let c=0; c<num[r].length; c++){
        process.stdout.write(`${num[r][c]}`);
        if(c!=num[r].length-1){
            process.stdout.write(' ');
        }
    }
    //process.stdout.write('\n');
    console.log();
}

console.log('======================================================================');



/*Jagged Array*/
let marks = [
    [1, 2, 3],
    [10],
    [23, 44, 55, 67],
    [90, 80]
]
for(let r=0; r<marks.length; r++){
    for(let c=0; c<marks[r].length; c++){
        process.stdout.write(`${marks[r][c]}`);
        if(c!=marks[r].length-1){
            process.stdout.write(' ');
        }
    }
    console.log();
}
