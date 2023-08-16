# 22m 33s

from collections import defaultdict

def solution(fees, records):
    # stack
    T_END = 23*60 + 59
    TimeBook = {}
    StackBook = defaultdict(int)
    
    for record in records:
        t, car_num, action = record.split()
        t = int(t[:2])*60 + int(t[3:])
        if action == "IN":
            TimeBook[car_num] = t
        else:  # "OUT"
            StackBook[car_num] += t - TimeBook[car_num]
            del TimeBook[car_num]
    
    for car_num, t in TimeBook.items():
        StackBook[car_num] += T_END - t
        
    # calculate
    answer = []
    time_min, fee_min, time_add, fee_add = fees
    car_nums = sorted(StackBook.keys())
    
    for car_num in car_nums:
        t = StackBook[car_num]
        if t <= time_min:
            answer.append(fee_min)
            continue
        else:
            t = t - time_min
            fee = fee_min + (t//time_add) * fee_add
            if t%time_add != 0:
                fee += fee_add
            answer.append(fee)
    
    return answer