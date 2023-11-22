def solution(s):
    answer = []
    end = True
    for i in s:
        if i == ' ':
            answer.append(i)
            end = True
            
        elif end:
            answer.append(i.upper())
            end = False
        
        else:
            answer.append(i.lower())
            end = False
    
    return "".join(answer)
        