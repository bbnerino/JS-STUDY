from collections import deque
def solution(n, m, section):
    answer = 0
    section = deque(section) # O(n), section 리스트를 deque로 변환하는 데 O(n) 시간이 걸림
    while section: # 최악의 경우, section의 모든 요소를 한 번씩 처리해야 하므로, O(n) 반복
        now = section.popleft()
        answer+=1
        while section and section[0]<now+m : # 최악의 경우, section의 모든 요소를 한 번씩 처리해야 하므로, O(n) 반복  
            section.popleft() # O(1)

    return answer

# 최악의 경우 O(n^2)

n = 8 # 총 길이 
m = 4 # 롤러 길이 
section = [2,3,6] # 색칠해야 할 곳

print(solution(n,m,section))