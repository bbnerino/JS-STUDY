# REACT 란?

- UI 구축을 위한 JS 라이브러리
- SPA 생성

| SPA 란?

Single Page Application으로
전체 페이지를 한번에 로드하고, 특정 부분만 ajax 요청으로 데이터 바인딩 하는 방법

## REACT 장점

- VDOM을 사용해 성능 향상
- CSR이 가능
- 컴포넌트의 가독성이 높고 간단해 유지보수가 쉬움

---

# 컴포넌트 란?

- 작은 단위로 만들어서 조립해서 사용하는 개발 방법

## 컴포넌트 장점

- 캡슐화, 확장성, 재사용성

---

# REACT의 내부 작동 원리

**_REACT 에서 DOM을 어떻게 렌더링하고 브라우저 이벤트를 처리하나요?_**
중간에 VDOM을 두어, VDOM이 변경될 때, 실제 DOM을 변경하도록 설계되어 있다.
이 작업을 'Reconcilation' 이라고 한다.

## DOM이란

# VDOM이란

실제 DOM의 변화를 최소화 시켜주는 역할
변화된 부분만 가려내, 한번의 렌더링이 가능하게 한다.

리액트가 실행되면, 컴포넌트들을 객체로 만들어 실행을 한다.
`createElement` 그리고 내용이 변경이 되면, 이 객체들의 변화를 보기 때문에 빠른 감지가 가능하다.

### VDOM 을 갱신시키는 법

setState 나 , store가 변하면 render() 함수를 호출하는 방식으로 갱신이 가능하다.

# 라이프 사이클

1. componentDidMount : 객체가 생성될 때 수행
2. render : 초기 화면을 그려줄 때와, 업데이트가 될 때 호출
3. componentDidupdate : 속성 값 또는 상태값이 변경되면 호출
4. componentWillunmount : 컴포넌트가 소멸될 때 호출

# Client Side Routing

웹 페이지의 렌더링이 브라우저 측에서 일어나는 것

# state가 불변성을 유지해야 하는 이유 (setState 사용 이유)

| 상태를 불변성을 띄게 변경한다. 이로 인해 **_객체의 주소값_**이 변경이 되면 변화가 된다.
state 를 직접 수정하면 render 함수를 호출하지 않는다.
state는 react의 객체형태 이다.

이 객체 형태를 변형 시키게 되면 기존의 값과 같은 참조값을 갖기 때문에, 변경이 되더라도 인식을 하지 못한다.

# Hook 이란?

함수형 컴포넌트에서 state와 생명주기 기능을 연동할 수 있는 함수이며
class 없이도 react를 사용할 수 있게 해주는 기능

- 상태값을 초기화
- 변경이 발생 시 훅함수 호출

# useState

state 값과 업데이트 하는 함수를 반환

# useEffect

DOM이 렌더링된 이후 어떤 일을 수행해야 하는지 명시하는 훅
함수내에 정의된 변수의 감지가 가능하다.
관심사의 분리가 가능해진다.

---

# Class Component, Function Component 차이점

라이프 사이클과 생명주기가 있었는데, hook을 사용해 생명주기에 원하는 동작을 하게 한다.

# JSX

JS 코드를 HTML 처럼 표현하는 언어
실행을 시키게 되면 H

# Map 에서 key 가 필요한 이유

VDOM이 변화된 내용을 찾는데, array를 순회하는 것보다 해시를 이용해서 하는 것이 빠르기 때문에 key가 필요하다.

# useMemo 이란

성능 최적화를 위해 사용되는 Hook
특정 결과를 재사용

# useCallback

특정 함수를 새로 만드는 것이 아닌 재사용할 때 사용
변수가 선언되어 지면, 함수가 실행된다.
값이 변경이 되면, 새로운 함수를 return 하고, 값이 변경되지 않으면 기존 함수를 Return 한다.

| 웹 성능 향상을 위해 useCallback을 사용했다~

# 상태 관리 라이브러리

props를 전달하는 단점을 해결하고자 store 라는 공간을 통해 데이터를 저장,
redux는 데이터가 한 방향으로 이동되어 진다.

# Redux 원리

1. action : redux를 움직이는 action으로 함수와 같은 개념이다.
2. reducer : 액션이 이뤄지면, state 데이터를 조작한다.

- action에서 reducer로 데이터나 실행명령을 전달하는 과정을 Dispatch 라고 한다.

3. store : 저장소

- store 에서 직접 컴포넌트로 데이터를 전달할 수 있는 것을 Selector 라고 한다.

# recoil 은?
