# L <= 1e4, W <= 1e4, N_trucks <= 1e4
# 시각 기준으로 체크하면, 최악의 경우, 1e4 * 1e4 = 1e8. => 가능은 하지 않나?
# 구현X(deque로 '다리 위 상태'를 기록하고, 아무도 못올라가는 때는 0으로 빈자리를 채워주면? N*L*2)
# 단축시키려면, 시각 기준으로 체크하지않는다. '다리 위 상태'기록 시, 진입한 시각을 씀으로써 다리를 나가는 시각을 유추할 수 있게 한다. 그럼 시간복잡도가 대략 트럭 개수 * 2일듯.

from collections import deque

def solution(bridge_length, weight, truck_weights):
    t = 0
    bridge_status = deque([])       # (weight, time_in)
    bridge_weight = 0
    truck_weights = deque(truck_weights)
    
    while truck_weights:
        # 구현 순서: 1) 빼기, 2) 넣기, 
        # 3) 넣기가 안되면, 시간 넘기기. 
        #   다리가 꽉 찬거면 +1, 
        #   무게가 꽉 찬거면 +(가장 앞 트럭이 빠져나갈 순간)
        
        if bridge_status and bridge_status[0][1] + bridge_length == t:      # 빼기
            w, _ = bridge_status.popleft()
            bridge_weight -= w
        
        avail_length = len(bridge_status) < bridge_length
        avail_weight = bridge_weight + truck_weights[0] <= weight
        
        if not avail_length:
            t += 1
        elif not avail_weight:
            t = bridge_status[0][1] + bridge_length
        else:
            w = truck_weights.popleft()
            bridge_status.append((w, t))
            bridge_weight += w
            t += 1
    
    if bridge_status:
        t = bridge_status[-1][1] + bridge_length + 1
    return t
            
            
    





"""
from collections import deque

def solution(bridge_length, weight, truck_weights):
    t = 0
    truck_weights = deque(truck_weights)
    ib_weights = deque([])
    ib_times = deque([])
    
    while truck_weights:
        print(t, ib_weights, ib_times)
        if (sum(ib_weights) + truck_weights[0] <= weight) and (len(ib_weights) < bridge_length):
            
            # time 1 step
            t += 1
            for i in range(len(ib_times)):
                ib_times[i] -= 1
            
            # add the next truck
            ib_times.append(bridge_length)
            ib_weights.append(truck_weights.popleft())
            
            # out if t=0_truck exist
            if ib_times[0] == 0:
                ib_times.popleft()
                ib_weights.popleft()
            
        else:   # now + next > weight   or   now_N full
            # time and pop the final truck
            t_temp = ib_times.popleft()
            ib_weights.popleft()
            t += t_temp
            for i in range(len(ib_times)):
                ib_times[i] -= t_temp
            
            if sum(ib_weights) + truck_weights[0] <= weight:
                ib_times.append(bridge_length)
                ib_weights.append(truck_weights.popleft())
    
    t = t + ib_times[-1]
    return t
    
"""