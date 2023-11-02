import sys

N, M = map(int, input().split())

keywords = set()

for n in range(N):
    keywords.add(sys.stdin.readline().strip())
number_of_n = len(keywords)

for m in range(M):
    kw = set(sys.stdin.readline().strip().split(','))
    for k in kw:
       if k in keywords:
           number_of_n -= 1
           keywords.remove(k) 
    print(number_of_n)
