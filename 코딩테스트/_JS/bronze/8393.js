const fs = require("fs");
const inputData = fs.readFileSync("./input.txt").toString();

let res = 0;
for (let i = 1; i <= inputData; i++) {
  res += i;
}
console.log(res);
