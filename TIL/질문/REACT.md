- useCallback/useMemo에 대해서 설명해주세요.
- 리액트에서 `setState`는 비동기 동작인가요, 동기동작인가요?
- `setState`가 비동기 동작을 취했을 때 얻을 수 있는 이점은 무엇인가요?
- 리액트의 `useCallback`, `useEffect`등을 사용할 때 의존성 배열을 받게 됩니다. 이 배열의 역할은 무엇인가요?
- 의존성 배열은 shallow equal, deep equal중 무엇을 하게 되나요?
- props로 전달받은 함수는, props나 상태가 업데이트될 때마다 새로 생성이 됩니다. 이 때 최적화할 수 있는 방법은 어떤게 있나요?
- 아래 코드의 경우, useCallback을 사용을 하더라도 isClicked 의존성을 가지고 있습니다. 이 경우, 아예 의존성이 없게 만드는 방법이 있나요?
```javascript
const handleToggle = useCallback(() => setIsClicked(!isClicked), [isClicked]);
```

- 다이나믹한 데이터를 받아올 때, useEffect에서 의존성배열을 어떻게 하실건가요?
- Next.js에서 `getStaticProps`, `getServerSideProps`의 차이점은?
- `useLayoutEffect`는 무엇인가요?
- 리액트를 사용할 때, 최적화에 신경쓰는 부분은 어떤 것이 있는지 구체적인 예시가 있나요?
- 아래와 같이 자식 컴포넌트를 React.memo로 감쌌을 때 props를 통해서 전달되어지는 함수에 useCallback을 사용한 경우와 사용하지 않은 경우에 차이가 있나요?
```javascript
function Parent(){
	const handleClick = useCallback(() => { ... }, []); // (1)
	const handleClick = () =>{ ... } // (2)

	return <Child onClick={handleClick} />
}

function Child({ onClick }) {
	return <div onClick={onClick} />
}
export default React.memo(Child); 
```


- React.memo의 특징에 대해서 설명해주세요.
- 얕은 비교(Shallow Equal)와 깊은 비교에 대해서 설명해주세요.
- React의 hook에 대해서 설명해주세요.
- 주로 어떤 경우에 custom hook을 사용했고, 그로 인해서 얻은 장점이 무엇인가요?
- Styled-components의 퍼포먼스에 대한 이슈에 대해서 경험해보신 적이 있나요?
- 리액트의 성능개선 방법에 대해서 설명해주세요.
- 상태 관리에 대해서 설명해주세요.