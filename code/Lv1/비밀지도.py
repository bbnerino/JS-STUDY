def solution(n, arr1, arr2):
    num1 = []
    num2 = []
    answer = []
    for num in arr1:
        str(bin(num))[2::]
        ar1 = str(bin(num))[2::]
        while len(ar1)<n:
            ar1 = "0"+ar1
        num1.append(list(ar1))
    
    for num in (arr2):
        ar2 = str(bin(num)[2::])
        while len(ar2)<n:
            ar2 = "0"+ar2
        num2.append(list(ar2))
        
        
    for i in range(len(num1)):
        res = ''
        for j in range(len(num1[i])):
            num = int(num1[i][j]) + int(num2[i][j])
            if num == 0:
                res+=" "
            else:
                res+="#"
        answer.append(res)
    
                
            
        
    return answer