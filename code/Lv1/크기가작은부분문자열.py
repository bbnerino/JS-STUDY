def solution(t, p):
    answer = 0
    len_p = len(p)
    p = int(p)
    for i in range(len(t)-len_p+1):
        
        if p >= int(t[i:i+len_p]):
            answer+=1

    return answer

t = "500220839878"	
p = "7"	

print(solution(t,p))