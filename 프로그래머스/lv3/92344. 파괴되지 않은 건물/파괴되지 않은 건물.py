# NM <= 1e6, S < 0.25 * 1e6 ~ 1e5
# [1] 정확성/ NM <= 1e4, event  <= 1e2 ==> O(N) 가능... 안되네?
# [2] 질문하기를 조금 보다가 힌트(누적합)를 조금 얻었다. (skills*N) + (NM) => ~2*1e6? 그래도 안되네
# [3] 결국 질문하기에 해설 봤는데, x방향 누적합 후, y방향 누적합을 하라고 되어 있다. (skills) + (NM)
# 2중으로 하는건 훨씬 생각해내기 어렵다..ㅠ
# 기본 제한사항으로 생각해보면 [1] O(NMS)~1e11, [2] O(SN+NM)~1e8, [3] O(S+NM*1~3)~1e6~7?
# 오해했던게, 제한 사항에서 정확성과 효율성을 제대로 안 봤다. 시간복잡도는 효율성에서 테스트될 것이므로 정확성 테스트와는 관련이 없다. 그래서 시간 초과가 발생

def solution(board, skill):
    # make relative board
    lenX = len(board[0])
    lenY = len(board)
    board_relative = [[0 for _ in range(lenX)] for _ in range(lenY)]
    
    for t, y1, x1, y2, x2, deg in skill:
        deg = deg if t == 2 else -deg
        x2 += 1
        y2 += 1
        
        board_relative[y1][x1] += deg
        if x2 < lenX: board_relative[y1][x2] -= deg
        if y2 < lenY: board_relative[y2][x1] -= deg
        if x2 < lenX and y2 < lenY: board_relative[y2][x2] += deg
    
    # make cumulative board
    count = 0
    for y in range(lenY):
        Xcumul = 0
        for x in range(lenX):
            Xcumul += board_relative[y][x]
            board_relative[y][x] = Xcumul

    Ycumuls = [0 for _ in range(lenX)]
    for y in range(lenY):
        for x in range(lenX):
            Ycumuls[x] += board_relative[y][x]
            board_relative[y][x] = Ycumuls[x]
            
    # find unbrokens
    count = 0
    for rels, oris in zip(board_relative, board):
        for rel, ori in zip(rels, oris):
            if rel + ori > 0:
                count += 1
                
    return count