# 어떤 선수는 직, 간접적으로 승패가 확인되면 순위가 결정된다.
# 간접을 어떻게 모두 체크할까.
# lose map, win map으로 하면 되려나.
# for 선수, lose 방향, win 방향으로 순회하면서 기록하기. => 100^2
# 더 효율적인 방법이 있을 것 같은데..

def solution(n, results):
    lose_map = [[] for _ in range(n)]   # lose_map[i] = [a, b, c]. i가 a, b, c에게 졌다.
    win_map = [[] for _ in range(n)]    # win_map[i] = [a, b, c]. i가 a, b, c에게 이겼다.
    for result in results:
        winner, loser = result
        winner -= 1
        loser -= 1
        lose_map[loser].append(winner)
        win_map[winner].append(loser)
    
    determined_map = [set() for _ in range(n)]  # i 선수와의 순위가 결정된 선수들
    
    for player in range(n):
        # lose map 순회
        stack = [player]
        while stack:
            j = stack.pop()
            for k in lose_map[j]:
                if k not in determined_map[player]:
                    determined_map[player].add(k)
                    stack.append(k)
        # win map 순회
        stack = [player]
        while stack:
            j = stack.pop()
            for k in win_map[j]:
                if k not in determined_map[player]:
                    determined_map[player].add(k)
                    stack.append(k)
    
    count = 0
    
    for player_set in determined_map:
        if len(player_set) == n - 1: count += 1
    return count