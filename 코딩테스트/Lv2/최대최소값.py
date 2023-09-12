def solution(s):
    num_list = list(map(int,s.split(" ")))
    num_list.sort()
    answer = ''
    answer += str(num_list[0]) + " "  + str(num_list[-1])
    
    return answer


# 뭐고~ 너무쉽네
