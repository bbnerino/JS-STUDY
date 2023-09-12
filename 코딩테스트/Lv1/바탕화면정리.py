wallpaper = [
    "..........", 
    ".....#....", 
    "......##..", 
    "...##.....", 
    "....#....."
    ]	

def solution(wallpaper):
    graph = [list(wall) for wall in wallpaper] # O(n*m)
 
    first = [-1,-1]
    last = [-1,-1]

    for i in range(len(graph)): # O(n)
        if "#" in graph[i]: # O(m)
            if first[0]<0:
                first[0] = i
            last[0] = i+1
        
    for j in range(len(graph[0])): # O(m)
        for i in range(len(graph)): # O(n)
            if graph[i][j] == "#": # O(1)
                if first[1]<0:
                    first[1] = j
                last[1] = j+1    

    answer = [first[0],first[1],last[0],last[1]]
    return answer
# O(m*n)

print(solution(wallpaper))