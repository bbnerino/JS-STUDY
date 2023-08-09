const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

const sum = input.reduce((a, b) => a + Number(b), 0);

console.log(sum);
