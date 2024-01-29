# brown <= 5e3, yellow <= 2e6
# w & h, b=2(w+h)-4, y=(w-2)(h-2)=wh-b
# y+b = wh, w+h=(b+4)/2

def solution(brown, yellow):
    sum_of_wh = (brown + 4) // 2
    prod_of_wh = brown + yellow
    
    for h in range(1, sum_of_wh//2 + 1):
        w = sum_of_wh - h
        if w*h == prod_of_wh:
            break
    
    answer = [w, h]
    return answer