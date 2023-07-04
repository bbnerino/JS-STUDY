def solution(players, callings):
    
    for calling in callings:
        index = players.index(calling)
        players[index-1],players[index] = players[index],players[index-1]

    return players
