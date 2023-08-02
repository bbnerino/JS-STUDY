# useState

Hook => render를 저절로 부르게끔 한다.

```js
setter (x){
  render()
}
```

```js
const useFetch = (api) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api(); // Assuming the API function returns a promise
        setData(response);
        setLoading(false);
      } catch (err) {
        setError(err);
        setLoading(false);
      }
    };

    fetchData();
  }, [api]);

  return { data, loading, error };
};

const UserList = () => {
  const { data, loading, error } = useFetch(UserService.getAllUsers);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h1>User List</h1>
      <ul>
        {data.map((user) => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
};
```
