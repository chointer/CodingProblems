# 순서 상관 없는 것인가?
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        stat_m = Counter(magazine)
        stat_r = Counter(ransomNote)
        
        for s, n in stat_r.items():
            if stat_m[s] - n < 0:
                return False
        
        return True