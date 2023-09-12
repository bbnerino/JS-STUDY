def solution(s, skip, index):
    alphabet = ["a","b","c","d","e",
                "f","g","h","i","j",
                "k","l","m","n","o",
                "p","q","r","s","t",
                "u","v","w","x","y",
                "z"]  
    
    answer = ''

    s = list(s)
    skip = list(skip)

    for al in skip : 
        alphabet.remove(al)

    result_alpha = {alpha:i for i,alpha in enumerate(alphabet)}
    result_num = {i : alpha for i,alpha in enumerate(alphabet)}

    for al in s :
        idx = result_alpha[al]
        str = result_num[(idx+index)%len(alphabet)]
        answer+=str
  
    return answer


s = "aukks"	
skip = "wbqd"	
index = 5
print(solution(s, skip, index))

