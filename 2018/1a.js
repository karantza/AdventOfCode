var fs = require('fs');
 
const input = fs.readFileSync('1.txt', 'utf8').split('\n');

const result = input.reduce((value, line) => value + parseInt(line), 0);

console.log(result);