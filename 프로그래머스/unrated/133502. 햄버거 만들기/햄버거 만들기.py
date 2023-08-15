from collections import deque

def solution(ingredient):
    if len(ingredient) <= 3: return 0

    ingredient = deque(ingredient)
    history = deque([])
    check = deque([ingredient.popleft() for i in range(3)])
    hamburger = deque([1, 2, 3, 1])
    count = 0
    
    while ingredient:
        check.append(ingredient.popleft())

        if check == hamburger:
            check.clear()
            count += 1
            
            while history and len(check) < 3:
                check.appendleft(history.pop())
                if check[0] == 1:
                    break
            while ingredient and len(check) < 3:
                check.append(ingredient.popleft())
            
        else:
            history.append(check.popleft())
        

    return count