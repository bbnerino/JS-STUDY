const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString();

list = input.split(" ").map((str) => Number(str));

const sum = list.reduce((a, b) => a + b);

console.log(sum);
