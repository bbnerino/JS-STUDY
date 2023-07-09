import math 
def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1) :
        a = math.floor((r2**2 - i**2)**0.5)
        b = math.ceil(max(0,r1**2 - i**2)**0.5)
        answer += a - b + 1
    return answer*4

r1 = 2
r2 = 3 

print(solution(r1,r2))

