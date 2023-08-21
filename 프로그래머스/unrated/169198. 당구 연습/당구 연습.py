# 예외 1) 코너 활용, 2) 경로에 공(수직, 수평)
# 질문에 코너는 고려 할 필요없다고 해서 생각해봤는데,
# 코너를 고려하는 경우는, 맞출 공과 코너 사이에 시작 공이 있는 경우이다.
# 해당 코너를 지나는 당구대 변은 2개, 그 변을 대칭으로 맞힐 공의 위치들과 코너점 대칭으로 맞힐 공의 위치와 기존 맞힐 공의 위치, 총 4개의 점으로 직사각형을 그리면 코너를 지나서 맞히는 거리는 변을 지나서 맞히는 거리보다 길다는 것을 알 수 있다.

# 37m 30s

def subsol(x_st, y_st, x_en, y_en, m, n, maxl):
    result = maxl
    
    # Vertical
    if x_st == x_en:
        if y_st < y_en:
            result = min(result, (y_st + y_en)**2)
        else:
            result = min(result, (2 * n - y_st - y_en)**2)
    else:
        result = min(result, (x_st - x_en)**2 + (y_st + y_en)**2)
        result = min(result, (x_st - x_en)**2 + (2 * n - y_st - y_en)**2)
    
    # Horizontal
    if y_st == y_en:
        if x_st < x_en:
            result = min(result, (x_st + x_en)**2)
        else:
            result = min(result, (2 * m - x_st - x_en)**2)
    else:
        result = min(result, (y_st - y_en)**2 + (x_st + x_en)**2)
        result = min(result, (y_st - y_en)**2 + (2 * m - x_st - x_en)**2)
        
    # Corner. slope check
    corners = [(0, 0), (m, 0), (0, n), (m, n)]
    for xc, yc in corners:
        L_s_c = (xc-x_st) ** 2 + (yc-y_st) ** 2
        L_c_e = (xc-x_en) ** 2 + (yc-y_en) ** 2
        if L_s_c < L_c_e and (xc-x_en) * (yc-y_st) == (yc-y_en) * (xc-x_st):
            result = min(result, L_s_c + L_c_e)
    
    return result
            
def solution(m, n, startX, startY, balls):
    maxl = m**2 + n**2
    answer = []
    for x_en, y_en in balls:
        answer.append(subsol(startX, startY, x_en, y_en, m, n, maxl))
    return answer