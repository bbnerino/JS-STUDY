const hash = {};
hash["key"] = "value";

console.log(hash["key"]); // value
console.log(hash.key); // value

// 문제 추천
// https://programmers.co.kr/learn/courses/30/lessons/42576

function solution(participant, completion) {
  const hash = {};
  participant.forEach((person) => { // O(N)
    if (hash[person]) {
      hash[person] += 1;
    } else {
      hash[person] = 1;
    }
  });
  completion.forEach((person) => { //O(N)
    if (hash[person]) {
      hash[person] -= 1;
    }
  });
  const keys = Object.keys(hash); // O(N)
  let result = "";
  Object.keys(hash).forEach((k) => { // O(N)
    if (hash[k] == 1) {
      result = k;
    }
  });

  // 공간 복잡도는 O(N)이다.
  // hash 객체는 참가자 수의 비례 O(N)만큼의 공간을 차지한다.
  // keys 배열은 참가자 수의 비례 O(N)만큼의 공간을 차지한다.

  return result;
}
