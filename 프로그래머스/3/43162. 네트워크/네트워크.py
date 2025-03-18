# n <= 200
# DFS/BFS로 풀어보기. stack DFS
def solution(n, computers):
    visited = [False for _ in range(n)]
    count = 0

    for i in range(n):
        if visited[i]:
            continue
        count += 1
        stack = [i]
        while stack:
            computer = stack.pop()
            if not visited[computer]:
                visited[computer] = True
                for neighbor, connected in enumerate(computers[computer]):
                    if connected and not visited[neighbor]:
                        stack.append(neighbor)
    return count