# 파이썬 코드를 JS로 고쳐보자

- pop() => pop()

- append() => push()

- sort()

- list(map(int,input.split())) => input.split(" ").map((str)=>Number(str))

- sum() => list.reduce((누적,현재)=> 누적+현재, 기본값 )

- count(array) => array.filter((arr)=>arr==n).length

- max(arr) => Math.max(...data)

- data[2::] => data.slice(2)
- data[2:4] => data.slice(2,4)

- 좌측 추가 : unshift(item)

# Reduce 이해하기

const numbers = [1,2,3,4]
const sum = numbers.reduce((누적,현재)=>누적+현재,기본값)

# 정렬하기

- list

- Object

# ... 함수

# Object 순회 🔥

```js
const keys = Object.keys(hash);
keys.forEach((k) => {
  hash[k];
});
```

# 암기하기

```js
// reduce
const sum = num_list.reduce((a, b) => a + b);

// 자르기
num_list[2:4] = num_list.slice(2,4)

// for of
for (word of word_list){clg(word)}

// for 문
for (let i=0;i<n ; i++){clg(i)}

// for in 문 => 이건 객체에서 사용하는 것 

// [0,0,0,0,0] 만들기
new Array(5).fill(0)

// findIndex 



```

# sort 

Object 를 Array 로 만들기 
const diceList = Object.entries(dice);
diceList.sort((a, b) => b[1] - a[1]);

people.sort((a,b)=>a.age -b.age) 
