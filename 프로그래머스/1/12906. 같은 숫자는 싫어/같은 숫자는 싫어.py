# N <= 1e6

def solution(arr):
    stack = [arr[0]]
    for a in arr[1:]:
        if stack[-1] != a:
            stack.append(a)
    return stack