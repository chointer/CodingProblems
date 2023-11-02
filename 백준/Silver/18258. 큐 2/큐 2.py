from collections import deque
from math import e
import sys

N = int(input())    # <= 2*10**6
q = deque()
l = 0

for n in range(N):
    cmdline = sys.stdin.readline().strip().split()
    cmd = cmdline[0]
       
    if cmd == "push":
        q.append(int(cmdline[1]))
        l += 1
        
    elif cmd == "pop":
        if q:
            l -= 1
            print(q.popleft())
        else:
            print(-1)
    
    elif cmd == "size":
        print(l)
    
    elif cmd == "empty":
        if q:
            print(0)
        else:
            print(1)
            
    elif cmd == "front":
        if q:
            print(q[0])
        else:
            print(-1)
        
    elif cmd == "back":
        if q:
            print(q[-1])
        else:
            print(-1)