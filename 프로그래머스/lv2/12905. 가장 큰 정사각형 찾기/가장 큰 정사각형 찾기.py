# 모르겠어서 단순하게 탐색 -> 시간 초과
# 힌트 참고 (DP) -> 시간 초과
# 거의 정답 참고 (2번째로 구현했던 것이 DP는 아니었던 것 같다.)
# (지금 위치까지의 최대 사각형 길이, 지금 위치에서의 최대 사각형 길이)를 저장했는데,
# 다른 풀이보면 지금 위치까지의 최대 사각형 길이는 그냥 상수 하나로 저장했어도 되었다.

def square(note1, note2, note3, val):
    maxlen_now = min(note1[1], note2[1], note3[1]) + 1 if val == 1 else 0
    maxlen = max(note1[0], note2[0], note3[0], maxlen_now)
    return (maxlen, maxlen_now)

from collections import defaultdict
def solution(board):
    notes = defaultdict(lambda:(0, 0))

    for y, bo in enumerate(board):
        for x, val in enumerate(bo):
            notes[(y, x)] = square(notes[(y-1, x-1)], notes[(y-1, x)], notes[(y, x-1)], val)
    return notes[(y, x)][0]**2