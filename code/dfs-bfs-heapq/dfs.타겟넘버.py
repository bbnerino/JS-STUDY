answer = 0

def solution(numbers, target):
    
    def recur(score,idx):
        global answer
        
        if idx == len(numbers):
            if score== target:
                answer+=1
        else:
            recur(score+numbers[idx],idx+1)
            recur(score-numbers[idx],idx+1)
    
    recur(0,0)
        
    return answer