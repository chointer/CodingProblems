import heapq

def solution(x, y, n):
    notes = {x: 0}
    candidates = [(x, 0)]

    while candidates:
        number, n_cal = heapq.heappop(candidates)
        n_cal_next = n_cal + 1
        
        for number_next in [number + n, number * 2, number * 3]:
            if number_next <= y and (number_next not in notes or notes[number_next] > n_cal_next):
                notes[number_next] = n_cal_next
                heapq.heappush(candidates, (number_next, n_cal_next))
        
    return -1 if y not in notes else notes[y]