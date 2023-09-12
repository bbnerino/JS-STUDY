def solution(name, yearning, photos):
    answer = []
    score = {}
    length = len(name)

    # name 리스트를 순회하여 딕셔너리(score)에 key-value 쌍을 저장하는데, O(n) 시간이 걸림
    for i in range(length):  
        score[name[i]] = yearning[i]
    
    # photos 리스트를 순회하는데, photos 리스트의 길이를 m이라고 할 때, O(m) 시간이 걸림
    for photo in photos :
        count = 0
        
    # photo 리스트를 순회하는데, photo 리스트의 평균 길이를 k라고 할 때, O(k) 시간이 걸림
        for user in photo :
            
            # 딕셔너리에서 특정 키를 검색하는데 O(1) 시간이 걸림
            if user in score:  
                count += score[user]
            
        answer.append(count)
    return answer

# 총시간 복잡도  O(n + m * k)