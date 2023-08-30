# 그냥 번갈아 가면서 떼면 최선? -> 아니다.
# DP?
# 31m 50s... N이 작은 경우를 고려하지 않아서 처음에 틀림.

from collections import deque

def subsol(stks):
    # notes = [ f(n-3), f(n-2), f(n-1) ]
    # inital: [ f(-1), f(0), f(1) ]
    notes = deque([0, stks.popleft(), stks.popleft()], maxlen=3)
    
    while stks:
        notes.append(max(notes[0], notes[1]) + stks.popleft())
    
    return max(notes)
    
def solution(sticker):
    if len(sticker) < 3:
        return max(sticker)
    return max(subsol(deque(sticker[:-1])), subsol(deque(sticker[1:])))