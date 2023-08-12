from collections import deque

def solution(order):
    N = len(order)
    order = deque(order)
    boxes = deque(range(1, len(order) + 1))
    saver = deque([])
    saver_size = 0
    
    while order:
        if boxes and order[0] == boxes[0]:
            order.popleft()
            boxes.popleft()
        elif saver and order[0] == saver[0]:
            order.popleft()
            saver.popleft()
        elif boxes:
            saver.appendleft(boxes.popleft())
        else:
            break
    
    return N - len(order)