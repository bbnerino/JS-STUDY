# 기존 코드 // 시간 초과
def solution(sequence, k):
    answer = []
    
    for i in range(len(sequence)):
        if sequence[i]>k:
            sequence = sequence[:i]
            break
    
    for i in range(1,len(sequence)+1): # 자리수 
        for j in range(len(sequence)-i+1):
            sum_num_list = sum(sequence[j:j+i])
            if (sum_num_list==k):
                return([j,j+i-1])
            if (sum_num_list>k):
                break
    
    return answer

# 모범 코드
# 투포인터
#  O(N)의 시간 복잡도
def solution(sequence,k):
    answer = []
    right = 0
    count = 0
    for left in range(len(sequence)): # for 루프 (N)
        while right<len(sequence) and count < k: # 최악이라도 N번 
            count += sequence[right]
            right+=1
        if count == k :
            if not answer: # 답이 비어있다면,
                answer = [left,right-1]
            else:
                if answer[1] - answer[0] > right - 1 - left: # 기존의 값이 더 긴지 이번게 더 긴지 확인
                  answer = [left, right-1] 
        count -= sequence[left] # 슬라이싱 윈도우 (다음 계산을 위해 맨 왼쪽 값 빼기)
    return answer        
sequence = [1, 1, 1, 2, 3, 4, 5]	
k = 5
right = 0 
count = 1 + 1 + 1 + 2 
print(solution(sequence,k))