function solution(a, b, c, d) {
  let dice = {};
  const list = [a, b, c, d];

  list.map((num) => {
    if (dice[num]) dice[num] += 1;
    else dice[num] = 1;
  });

  const diceList = Object.entries(dice);
  diceList.sort((a, b) => b[1] - a[1]);

  if (diceList[0][1] == 1) {
    return list.reduce((a, b) => (a < b ? a : b));
  }
  if (diceList[0][1] == 3) {
    return (10 * diceList[0][0] + Number(diceList[1][0])) ** 2;
  }
  if (diceList[0][1] == 4) {
    return 1111 * diceList[0][0];
  }
  if (diceList[0][1] == 2) {
    if (diceList[1][1] == 2) {
      const a = Number(diceList[1][0]);
      const b = Number(diceList[0][0]);
      const result = (a + b) * (a - b);
      if (result > 0) return result;
      else return -result;
    } else {
      return diceList[1][0] * diceList[2][0];
    }
  }
}

console.log(solution(2, 2, 2, 2));
