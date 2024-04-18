# 2**20 ~ 10**6
# DFS
def solution(numbers, target):
    # (now, list_left)
    count = 0
    stack = [(0, numbers)]

    while stack:
        now, lefts = stack.pop()
        if not lefts:   # end case
            if now == target:
                count += 1
            else:
                continue
        
        else:
            stack.append((now + lefts[0], lefts[1:]))
            stack.append((now - lefts[0], lefts[1:]))
    return count







"""
def func(nums, tar, val, idx):
    if idx == -1:
        return 1 if val == tar else 0
    
    return func(nums, tar, val+nums[idx], idx - 1) + func(nums, tar, val-nums[idx], idx - 1)
            
def solution(numbers, target):
    return func(numbers, target, 0, len(numbers)-1)
"""