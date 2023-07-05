def solution(keymap, targets):
    answer = []
    keyword = {}
    for kmap in keymap: # O(n)
        kmap = list(kmap)
        for i in range(len(kmap)):  # O (m)
            count = keyword.get(kmap[i],100)
            if count > (i+1) :
                keyword[kmap[i]] = i+1
    
    for target in targets: # O(k)
        count = 0
        target = list(target)
        for t in target: # O(j)
            try :
              count+= keyword[t]
            except:
              count = -1
              break
        answer.append(count)   
    return answer
# O(n*m + k*j)

keymap = ["ABACD", "BCEFD"]	
targets = ["ABCD","AABB"]	
print(solution(keymap,targets))