var fs = require("fs");
const input = fs.readFileSync("2.txt", "utf8").split("\n");

const numChars = input.map(x => {
  const chars = x.split("");
  const occur = {};
  chars.forEach(c => {
    if (c in occur) occur[c]++;
    else occur[c] = 1;
  });
  return Object.values(occur);
});

const duplicates = numChars.filter(x => x.includes(2));
const triplicates = numChars.filter(x => x.includes(3));

console.log(duplicates.length * triplicates.length);