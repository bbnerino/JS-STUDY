def solution(number, limit, power):
    answer = 0
    dp = [0 for _ in range(number+1)]
    
    def sosu(num):
        count = 1
        for i in range(1,target//2+1):
            if num%i ==0:
                count+=1
        if count>limit:
            return power
        else:
            return count 
    
    dp[1] = 1
    
    for target in range(1,number+1):
        if dp[target] == 0:
            count = sosu(target)
            dp[target] = count
            
    answer= sum(dp)
            
        
    return answer