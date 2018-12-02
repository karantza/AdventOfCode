var fs = require("fs");
const input = fs.readFileSync("2.txt", "utf8").split("\n");


function compare(a, b) {
    var common = "";
    var diffs = 0;
    for (i = 0; i < a.length; i++) {
        if (a[i] == b[i]) common += a[i];
        else diffs++;
        if (diffs > 1) return null;
    }
    if (diffs == 0) return null;
    return common;
}

function run() {
    for (let i = 0; i < input.length; i++) {
        for (let j = i+1; j < input.length; j++) {
            const x = compare(input[i], input[j]);
            if (x) {
                return x;
            }
        }
    }
}

console.log(run());