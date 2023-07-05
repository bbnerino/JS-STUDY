

# 기존 코드 

def solution(players, callings):
    
    for calling in callings:
        # 리스트에서 호출하는 항목을 찾는데 O(n) 시간이 걸림 
        index = players.index(calling)  
        # 인접한 값들을 바꾸는데 O(1) 시간이 걸림
        players[index-1], players[index] = players[index], players[index-1]  

    return players

# 최대 O(n * m) 시간이 소요된다. 
# n 은 players m 은 callings 


def solution(players, callings):

    result = { player:i for i, player in enumerate(players)}
    # {'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}
    # 딕셔너리 생성은 O(n) 시간이 걸림

    for calling in callings:
        
        # 딕셔너리를 이용하여 호출하는 항목의 인덱스를 찾는데 O(1) 시간이 걸림
        index = result[calling]

        # 딕셔너리의 값 수정은 O(1) 시간이 걸림
        result[calling] -=1 
        result[players[index-1]] += 1
        
        # 인접한 값들을 바꾸는데 O(1) 시간이 걸림
        players[index], players[index-1]  = players[index-1],players[index]
    
    return players


# 최대 O(m) 시간이 소요된다.