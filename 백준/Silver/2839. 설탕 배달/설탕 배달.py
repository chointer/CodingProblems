# N <= 5000
# f(N) = min( f(N-3), f(N-5) ) + 1

def f(N, dictionary):
    result = 5000
    if N-3 in dictionary.keys():
        result = dictionary[N-3]
    
    if N-5 in dictionary.keys():
        result = min(result, dictionary[N-5])
    
    if result != 5000:
        dictionary[N] = result + 1
    return dictionary


dictionary = {3:1, 5:1}

N = int(input())

for n in range(1, N + 1):
    f(n, dictionary)

    
if N in dictionary.keys():
    print(dictionary[N])
else:
    print(-1)