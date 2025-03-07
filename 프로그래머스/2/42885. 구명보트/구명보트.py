# N(people) < 50000, 40~240kg -> 계수 정렬
# 계수정렬 => O(N)
# 가벼운 사람은 최대한 잘 활용해야한다.
# 무거운 사람부터 해결해야한다.
# people sort(무게 내림차순), 보트 빈 무게 heapq (빈 무게 내림차순)
# 가장 큰 "보트 빈 무게"에 못 넣으면 어차피 못 넣는다.
# NlogN + NlogN
# 아아아 최대 2명 탑승이었다.

import heapq as hq

def solution(people, limit):
    people = sorted(people, reverse=True)
    boats = []
    boat_doubled = 0
    
    for p in people:
        if not boats or -boats[0] < p:   # 남은 자리보다 더 무거우면,
            hq.heappush(boats, -(limit - p))
        else:
            hq.heappop(boats)
            boat_doubled += 1
            
    return len(boats) + boat_doubled