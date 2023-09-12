const fs = require("fs");
const inputData = fs.readFileSync("./input.txt").toString().split("\n");

const before = inputData[0].split(" ").map((t) => +t);

const flow = +inputData[1];

let after = {
  hour: before[0],
  min: before[1] + flow,
};

몫 = Math.floor(after.min / 60);
나 = after.min % 60;

after = {
  hour: (after.hour + 몫) % 24,
  min: 나,
};

console.log(after.hour, after.min);
