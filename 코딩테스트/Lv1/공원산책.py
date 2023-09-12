def solution(park, routes):
    
    graph = [list(row) for row in park]
    start = [0,0]
    

    # O(n * m)
    for i in range(len(graph)): 
        for j in range(len(graph[i])):
            if graph[i][j] == "S": 
                graph[i][j] =="O"
                start = [i,j]
    
    # 방향 벡터 정의
    #    S  N  E  W 
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    
    # O(k)
    for route in routes:
        dir,count = route.split(" ")
        vector = {"S":0,"N":1,"E":2,"W":3}.get(dir,4)
        
        flag = True
        for c in range(1,int(count)+1):
            ny = start[0] + dy[vector] * c
            nx = start[1] + dx[vector] * c
            if 0<=ny<len(graph) and 0<=nx<len(graph[0]) :
                if graph[ny][nx] == "X" :
                    flag = False
                    break
            else : 
                flag = False
        if flag:
            start[0] = start[0] + dy[vector]*int(count)
            start[1] = start[1] + dx[vector]*int(count)
                              
    return start

# O(n*m + k)