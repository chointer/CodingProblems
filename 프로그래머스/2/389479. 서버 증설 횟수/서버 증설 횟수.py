# 이용자 [ n*m, (n+1)*m ) -> 최소 n 대 증설된 서버. k시간 운영 후 반납.
# h=24
# 시간마다 현 서버와 이용자 수를 보고 필요한 서버 수 체크. (Greedy? 반례가 있나?)
# O(N) = 24*k
"""
nm <= p < (n+1)m
n <= p/m < n+1
"""    
    
def solution(players, m, k):
    count = 0
    hours = len(players)
    servers_n = [0 for _ in range(hours)]
    
    for i, p in enumerate(players):
        servers_req = p // m
        
        servers_add = servers_req - servers_n[i]
        if servers_add > 0:
            count += servers_add
            for j in range(i, min(i + k, hours)):
                servers_n[j] += servers_add
        
    return count