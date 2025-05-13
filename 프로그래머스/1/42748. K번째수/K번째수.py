# arr <= 1e2, command <= 50
# slice + sort -> arr + arr log arr 

def solution(array, commands):
    answer = []
    for (i, j, k) in commands:
        arr = sorted(array[i-1: j])
        answer.append(arr[k-1])
    return answer
    
"""
def solution(array, commands):
    answer = []
    for coms in commands:
        i, j, k = coms
        answer.append(sorted(array[i-1:j])[k-1])
    return answer
"""