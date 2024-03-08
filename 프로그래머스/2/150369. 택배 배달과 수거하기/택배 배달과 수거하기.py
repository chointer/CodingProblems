# n <= 1e5
# n * 100 <= 1e7
# 가장 먼 곳은 언젠간 가야한다. 가장 먼 곳부터 차례대로 처리?

def solution(cap, n, deliveries, pickups):
    max_delivery = n - 1
    max_pickup = n - 1
    while max_delivery >= 0:
        if deliveries[max_delivery] == 0:
            max_delivery -= 1
        else:
            break
    
    while max_pickup >= 0:
        if pickups[max_pickup] == 0:
            max_pickup -= 1
        else:
            break
    
    
    answer = 0

    while max_delivery >= 0 or max_pickup >= 0:
        answer += (max(max_delivery, max_pickup) + 1) * 2
        box = cap
        while max_delivery >= 0 and box > 0:
            if box >= deliveries[max_delivery]:
                box -= deliveries[max_delivery]
                deliveries[max_delivery] = 0
            else:
                deliveries[max_delivery] -= box
                box = 0
            while max_delivery >= 0 and deliveries[max_delivery] == 0:
                max_delivery -= 1

            
        box = cap
        while max_pickup >= 0 and box > 0:
            if box >= pickups[max_pickup]:
                box -= pickups[max_pickup]
                pickups[max_pickup] = 0
            else:
                pickups[max_pickup] -= box
                box = 0
            while max_pickup >= 0 and pickups[max_pickup] == 0:
                max_pickup -= 1

    return answer