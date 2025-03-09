# N(citations) < 1e3, 인용 횟수 < 1e4
# sort(citations, reverse), for c, idx-th 논문의 인용 횟수가 idx보다 크면 h 가능
# O(N) = N log N + N

def solution(citations):
    citations.sort(reverse=True)
    h_max = 0
    
    for i, c in enumerate(citations, start=1):
        if i <= c:
            h_max = i
    return h_max