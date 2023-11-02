# 최소 h 논문이 h번 cited
# n <= 5 * 10**3

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        citations.sort(reverse=True)

        for i, cites in enumerate(citations, start=1):
            if i <= cites:
                h = i
            else:
                break
        
        return h