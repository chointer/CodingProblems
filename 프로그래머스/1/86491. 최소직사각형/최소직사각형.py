# N <= 1e4
# 긴 방향으로 정렬한 뒤, 튀어나온 것을 눕혀보는 방법이 가능할까?
# 완전탐색이 되는건가?

def solution(sizes):
    ws = []
    hs = []
    for i, (w, h) in enumerate(sizes):
        if w < h:
            w, h = h, w
        ws.append(w)
        hs.append(h)
        
    
    area = max(ws) * max(hs)
    for i, (w, h) in enumerate(zip(ws, hs)):
        ws[i] = h
        hs[i] = w
        new_area = max(ws) * max(hs)
        if new_area <= area:
            area = new_area
        else:
            ws[i] = w
            hs[i] = h
            
    return area