# query <= 1e6
# N log N

import heapq as hq
from collections import defaultdict

def solution(operations):
    # heapq
    asc = []
    desc = []
    
    # lazy deletion. 숫자마다 지워야 할 갯수 저장
    todo_asc = defaultdict(int)
    todo_desc = defaultdict(int)

    for operation in operations:
        oper, obj = operation.split()
        obj = int(obj)
        
        if oper == 'I':         # insert
            hq.heappush(asc, obj)
            hq.heappush(desc, -obj)
            
        elif oper == 'D':       # delete
            # 빈 큐일 때 데이터 무시하는 것은 while 문에서 처리될 듯            
            if obj == 1:        # delete max
                while desc:
                    pop = -hq.heappop(desc)
                    if todo_desc[pop] > 0:
                        todo_desc[pop] -= 1
                    else:
                        todo_asc[pop] += 1
                        break
                
            elif obj == -1:     # delete min
                while asc:
                    pop = hq.heappop(asc)
                    if todo_asc[pop] > 0:
                        todo_asc[pop] -= 1
                    else:
                        todo_desc[pop] += 1
                        break
        
    # 마지막 정리
    while desc:
        if todo_desc[-desc[0]] > 0:
            todo_desc[-desc[0]] -= 1
            hq.heappop(desc)
        else:
            break
    
    while asc:
        if todo_asc[asc[0]] > 0:
            todo_asc[asc[0]] -= 1
            hq.heappop(asc)
        else:
            break
    
    answer_max = 0 if not desc else -desc[0]
    answer_min = 0 if not asc else asc[0]
    return (answer_max, answer_min)