- 2진법 사용법
`a = bin(c)`
`int(a, 2)`



```python
def ten_to_N(num,N):
    ans = ""
    maxi = 0
    
    for i in range(num):
        if N**i > num:
            break
        else:
            maxi = i
    
    for i in range(maxi,-1,-1):
        tmp = 0
        for j in range(1,N):
            if (N**i)*j <= num:
                tmp = j
            else :
                break
        num -= (N**i)*tmp
        ans += str(tmp)
```