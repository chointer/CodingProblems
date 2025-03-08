# n < 1e3
# for (1, n+1), n번 => O(N) = N**2
# k개의 합으로 반복하는게 아니라, k부터 시작하는 합들을 보면 index 횟수를 줄일 수 있을 것 같다.

def solution(elements):
    elements_length = len(elements)
    answer = set()
    elements_long = elements + elements
    
    for i in range(len(elements)):
        elements_part = elements_long[i:i + elements_length]
        summ = 0
        for el in elements_part:
            summ += el
            answer.add(summ)
    
    return len(answer)