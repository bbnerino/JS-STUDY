const fs = require("fs");
const inputData = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map((d) => +d);

// 3개 => 10000원 + 같은거 1000
// 2개 => 1000 + 같은거 100
// 다 다름 => 다른거 100

count = 0;
maxi = 0;

inputData.map((num) => {
  const cnt = inputData.filter((d) => d === num).length;
  if (cnt > count) {
    count = cnt;
    maxi = num;
  }
});

if (count === 1) {
  return console.log(Math.max(...inputData) * 100);
}
if (count === 2) {
  return console.log(1000 + maxi * 100);
}
if (count === 3) {
  return console.log(10000 + maxi * 1000);
}

