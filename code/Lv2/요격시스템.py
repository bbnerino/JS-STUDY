def solution(targets):
    answer = 0
    targets.sort(key=lambda x:(x[0],x[1]))
    start = 0
    end = 0
    for [s,e] in targets:
      if end <= s :
        answer+=1
        start = s
        end = e  
      if e < end:
         end = e     
    return answer

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))

# [[1, 4], [3, 7], [4, 5], [4, 8], [5, 12], [10, 14], [11, 13]]
# [4, 5], [4, 8], [5, 12], [10, 14], [11, 13]]
# [4, 5], [5, 12], [10, 14], [11, 13]]