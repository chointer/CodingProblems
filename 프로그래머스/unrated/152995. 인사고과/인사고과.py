# 모든 사원에 대해 인센티브를 못받는 경우를 걸렀더니 시간 초과
# 모든 사원의 등수를 구하지 말고, 완호에 대해서만 집중해보기로 함. -> 이미 확인한, 등수 높은 사원이 인센티브를 못받는 경우가 생길 수 있다.
# 질문하기를 봤더니, 음... 각 태도 점수별 최대 동료 점수를 저장하고 비교에 사용한다. -> 안 된다.
# 정답 게시물 확인. 순차 체크하되, 체크한 사원이 나중에 reject되는 일이 없도록 정렬한다.
# -> 태도 점수 내림차순, 동료 점수 오름차순으로 정렬. 가장 높은 동료 점수를 저장하여 그 다음 태도 점수에서 사용한다? 동료 점수를 오름차순으로 정렬하면 해당 태도 점수에서 최대 점수가 갱신되어도 사용되지 않는다.
# 너무 어려웠다.

def solution(scores):
    mysc1, mysc2 = scores.pop(0)
    myscore_sum = mysc1 + mysc2
    rank = 1
    
    scores.sort(key = lambda x: (-x[0], x[1]))
    sc_max = 0
    
    for sc1, sc2 in scores:
        # reject
        if sc_max > sc2:
            continue
        
        sc_max = sc2
        
        if sc1 > mysc1 and sc2 > mysc2:
            return -1
        
        if sc1 + sc2 > myscore_sum:
            rank += 1
        
    return rank