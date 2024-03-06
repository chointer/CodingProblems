# user_id <= 8, string <= 8
# 불량 아이디에 들어갈 수 있는 아이디를 찾고,
# 완전 탐색?

def is_matched(ban, user):
    if len(ban) != len(user):
        return False
    
    for b, u in zip(ban, user):
        if b != "*" and b != u:
            return False
    
    return True

    
def solution(user_id, banned_id):
    # mapping
    candidates = {ban: [] for ban in banned_id}
    for ban in candidates:
        for user in user_id:
            if is_matched(ban, user):
                candidates[ban].append(user)
    
    # search
    answer_sets = set()
    stack = [([], banned_id, user_id)]
    while stack:
        banned, to_ban, lefts = stack.pop()
        
        if not to_ban:
            answer_sets.add(tuple(sorted(banned)))
            continue
        
        for c in candidates[to_ban[0]]:
            if c in lefts:
                lefts.remove(c)
                stack.append((banned + [c], to_ban[1:], lefts.copy()))
                lefts.append(c)
    
    return len(answer_sets)