class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        answer = True
        word_dict = dict()
        word_set = set()
        
        s_split = s.split()
        if len(pattern) != len(s_split):
            return False
        
        for p, w in zip(pattern, s_split):
            if p not in word_dict:
                if w in word_set:
                    answer = False
                    break
                else:
                    word_dict[p] = w
                    word_set.add(w)

            elif word_dict[p] != w:
                answer = False
                break
                
        return answer
        