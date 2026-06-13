
let str = 'Sachin Ade';
let charArr = str.replace(/\s/g, '').split('');
let obj = charArr.reduce((acc, char) => {
    acc[char] = (acc[char] || 0) + 1;
    return acc;
}, {});
console.log(JSON.stringify(obj));
