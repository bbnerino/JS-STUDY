def solution(s):
    str_list = s.split(" ")
    
    for i in range(len(str_list)) :
        text = str_list[i].capitalize()
        str_list[i] = text
    answer = " ".join(str_list)
    
    return answer