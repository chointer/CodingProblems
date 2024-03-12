# t <= 1000 -> 단순히 시간에 따라 계산해도 되겠다.

from collections import deque

def solution(bandage, health, attacks):
    max_health = health
    attacks = deque(attacks)
    t = 0
    stack = 0
    
    while attacks:
        if attacks[0][0] == t:
            t_attack, damage = attacks.popleft()
            health -= damage
            stack = 0
            if health <= 0:
                return -1
        else:
            stack += 1
            health += bandage[1]
            if stack == bandage[0]:
                health += bandage[2]
                stack = 0
            if health > max_health:
                health = max_health

        t += 1
        
    return health