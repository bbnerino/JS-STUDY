const fs = require("fs");
const inputData = fs.readFileSync("./input.txt").toString().split("\n");
const target = +inputData[0];

const data = inputData.splice(2).map((d) => d.split(" "));

const res = data.reduce((a, li) => a + +li[0] * +li[1], 0);

console.log(res === target ? "Yes" : "No");
