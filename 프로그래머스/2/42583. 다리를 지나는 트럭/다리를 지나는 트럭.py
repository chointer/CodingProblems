# L <= 1e4, N <= 1e4
from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    
    t = 0
    weight_current = 0
    state = deque()
    
    while truck_weights:
        t += 1

        if state and state[0][1] <= t:
            weight_current -= state.popleft()[0]
            
        if weight_current + truck_weights[0] <= weight:
            w = truck_weights.popleft()
            state.append((w, t + bridge_length))
            weight_current += w
        
    return state[-1][-1]