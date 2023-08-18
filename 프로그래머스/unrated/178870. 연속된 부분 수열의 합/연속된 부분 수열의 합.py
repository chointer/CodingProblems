from collections import deque

def solution(sequence, k):
    sequence = deque(sequence)
    subseq = deque([sequence.popleft()])
    st = 0
    en = 1
    val = subseq[0]
    answers = []
    
    while sequence:
        while val > k:
            val -= subseq.popleft()
            st += 1
        
        if val == k:
            answers.append([st, en])
        
        subseq.append(sequence.popleft())
        val += subseq[-1]
        en += 1
            
    while subseq:
        if val == k:
            answers.append([st, en])
        val -= subseq.popleft()
        st += 1
        
    answers.sort(key = lambda x: (x[1]-x[0], x[0]))
    answer = answers[0]
    answer[1] -= 1
    
    return answer