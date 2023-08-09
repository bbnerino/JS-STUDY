// reduce 를 구현해보기

const list = [1, 2, 3, 4, 5];

const reduceMoon = (list, callback, initValue) => {
  let result = initValue;
  list.forEach((item) => {
    result = callback(result, item);
  });
  return result;
};

const res = reduceMoon(list, (a, b) => a + b, 0);

console.log(res);

