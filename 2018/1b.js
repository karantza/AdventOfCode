var fs = require('fs');
 
const input = fs.readFileSync('1.txt', 'utf8').split('\n');

var found = {}

var i = 0;
var freq = 0;

while (true) {
    var idx = i % input.length;
    freq += parseInt(input[idx]);
    if (freq in found) {
        console.log(`Duplicate detected, index ${idx} value ${freq}`);
        break;
    }
    found[freq] = true;
    i++;
}
