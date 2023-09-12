import heapq
def solution(maps):
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    Q = []
    heapq.heappush(Q,[1,0,0])
    maps[0][0] = 0
    
    while Q :
        count,y,x = heapq.heappop(Q)
        if y== len(maps)-1 and x ==len(maps[0])-1:
            return count

        for i in range(4):
            ny = dy[i]+y
            nx = dx[i]+x
            if 0<=ny<len(maps) and 0<=nx<len(maps[0]):
                if maps[ny][nx] == 1:
                    heapq.heappush(Q,[count+1,ny,nx])
                    maps[ny][nx] = 0
                        
        
    return -1