# arr <= 100, commands <= 50
# cmd * arr*log(arr) ~ 50*100*2 = 1e5

def solution(array, commands):
    answer = []
    
    for st, en, k in commands:
        answer.append( sorted(array[st - 1 : en])[k-1] )

    return answer