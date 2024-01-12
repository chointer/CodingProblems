# N_prog <= 100

def solution(progresses, speeds):
    answer = []
    firstDay = 0
    count = 0
    
    for p, s in zip(progresses, speeds):
        left = 100 - p
        days = left//s if left%s == 0 else left//s + 1
        if count == 0:              ## Initial Case
            count += 1
            firstDay = days
        elif days <= firstDay:      ## count != 0
            count += 1
        else:                       ## days > firstDay
            answer.append(count)
            firstDay = days
            count = 1
    
    answer.append(count)
    return answer