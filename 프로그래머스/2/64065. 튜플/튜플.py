# len(s) <= 1e6
# 배열 길이 <= 500
# 정답 튜플은 중복 원소가 없으므로 set으로 구현해도 된다.
# s를 split하고, 길이로 sort. 작은 순서대로, set으로 표현 후 처리

def parse(s):
    s = s[2:-1]
    seq = s.split('{')

    sets = []
    for sub_seq in seq:
        sub_seq = sub_seq.split('}')[0]
        sub_seq = sub_seq.split(',')
        sub_seq = set(map(int, sub_seq))
        sets.append(sub_seq)
    return sorted(sets, key=len)
    
    
def solution(s):
    answer = []
    
    # parsing
    sets = parse(s)
    
    s0 = set()
    for s in sets:
        answer.append((s-s0).pop())
        s0 = s
    
    return answer