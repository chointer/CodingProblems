# board <= (7, 7)
def solution(board, h, w):
    count = 0
    color = board[h][w]
    n = len(board)
    
    for dh, dw in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        hh = h + dh
        ww = w + dw
        if hh >= 0 and hh < n and ww >= 0 and ww < n and board[hh][ww] == color:
            count += 1
            
    return count