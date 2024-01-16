# records <= 1e3
# dict로 차량 관리 O(1e3), 끝나면 순서대로 계산 O(1e3)

from collections import defaultdict

def fee_cal(t, fees):
    fee = fees[1]
    exceeded_time = t - fees[0]
    if exceeded_time > 0:
        fee += exceeded_time//fees[2] * fees[3]
        if exceeded_time%fees[2] > 0:
            fee += fees[3]
    return fee
        
def hm_to_m(t):
    h, m = map(int, t.split(':'))
    return h*60 + m

def solution(fees, records):
    TIME_END = hm_to_m("23:59")
    
    car_time_in = dict()                # car_number: time_in
    car_time_stack = defaultdict(int)   # car_number: time_stacked
    
    for record in records:
        t, car_number, inout = record.split()
        car_number = int(car_number)
        if inout == "IN":
            car_time_in[car_number] = hm_to_m(t)
        else:
            car_time_stack[car_number] += hm_to_m(t) - car_time_in[car_number]
            car_time_in[car_number] = -1
    
    answer = []
    for car in sorted(list(car_time_in.keys())):
        if car_time_in[car] >= 0:
            answer.append(fee_cal(car_time_stack[car] + TIME_END - car_time_in[car], fees))
        else:
            answer.append(fee_cal(car_time_stack[car], fees))

    return answer