# m + n <= 200
from collections import deque

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        elif n == 0:
            return

        q1 = deque(nums1[:m])
        q2 = deque(nums2)
        answer = []
        
        a = q1[0]
        b = q2[0]

        while q1 and q2:
            if a <= b:
                answer.append(a)
                q1.popleft()
                if q1:
                    a = q1[0]
            else:
                answer.append(b)
                q2.popleft()
                if q2:
                    b = q2[0]
        
        if q1:
            answer = answer + list(q1)
        elif q2:
            answer = answer + list(q2)
        
        for i in range(n + m):
            nums1[i] = answer[i]