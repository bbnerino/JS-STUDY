def solution(today, terms, privacies):
    answer = []
    DEFAULT_DAY = 28

    def calculate_date(date):
        date_list = list(map(int,date.split(".")))
        return date_list[0]*DEFAULT_DAY*12 + date_list[1]*DEFAULT_DAY + date_list[2]

    today = calculate_date(today)

    term_date ={}
    for term in terms:
        name,day = term.split(" ")
        day = int(day)*DEFAULT_DAY
        term_date[name] = day

    for i in range(len(privacies)) :
        
        day,term = privacies[i].split(" ")
        day = calculate_date(day)

        if today >= day + term_date[term]:
            answer.append(i+1)

    return answer

# 모든달 28

today = "2022.05.19"	
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today,terms,privacies))