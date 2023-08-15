# 13 * 12 * 11 / 3! < 1000
def solution(number):
    answer = 0
    for i, n1 in enumerate(number):
        for j, n2 in enumerate(number[i+1:], start = i+1):
            for k, n3 in enumerate(number[j+1:], start = j+1):
                if sum([n1, n2, n3]) == 0:
                    answer += 1
    return answer