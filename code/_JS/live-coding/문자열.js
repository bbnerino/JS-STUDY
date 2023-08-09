var list = ["a", "b", "c", "d", "e", "f", "b", "c", "d", "e", "f"];

// 1. for문
const forMoon = (list) => {
  for (let i = 0; i < list.length; i++) {
    if (list[i] === "c") {
      break;
    }
    console.log(list[i]);
  }
};
// forMoon(list);

// 2. forEach
const forEachMoon = (list) => {
  list.forEach((item) => {
    console.log(item);
  });
};
forEachMoon(list);

// 3. map
const mapMoon = (list) => {
  list.map((item) => {
    console.log(item);
  });
};

// mapMoon(list);

// 4. for of
const forOfMoon = (list) => {
  for (const item of list) {
    console.log(item);
  }
};

// forOfMoon(list);

// 5. for in 은 객체의 속성을 반복한다. 
const forInMoon = (list) => {
  for (const item in list) {
    console.log(item);
  }
};

// forInMoon(list); // 숫자가 나옴

// 6. while
const whileMoon = (list) => {
  let i = 0;
  while (i < list.length) {
    console.log(list[i]);
    i++;
  }
};

// whileMoon(list);

// reverse
const reverseMoon = (list) => {
  for (let i = list.length - 1; i >= 0; i--) {
    console.log(list[i]);
  }
};

// reverseMoon(list);

const resverseMoon2 = (list) => {
  const reverseList = [];
  list.forEach((item) => {
    reverseList.unshift(item);
  });
  console.log(reverseList);
};
// resverseMoon2(list);

const resverseMoon3 = (list) => {
  const reverseList = [];
  while (list.length > 0) {
    reverseList.push(list.pop());
  }
  console.log(reverseList);
};
// resverseMoon3(list);

const duplicateMoon = (list) => {
  const duplicateList = [];
  const count = {};
  // includes 없이
  list.forEach((item) => {
    if (count[item]) {
      count[item] += 1;
    } else {
      count[item] = 1;
      duplicateList.push(item);
    }
  });

  console.log(count);
};

duplicateMoon(list);

