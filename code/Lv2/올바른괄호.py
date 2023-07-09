from collections import deque
def solution(s):
    Q = deque([])
    items = list(s)
    for item in items:
        if item=="(":
            Q.append(item)
        else:
            if Q and Q[-1]=="(":
                Q.pop()
            else:  
                return False
    if Q:
        return False
    
    return True