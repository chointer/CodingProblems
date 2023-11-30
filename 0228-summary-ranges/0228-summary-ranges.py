# nums.length <= 20

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answers = []
        post = 2**31
        st = -1
        en = -1
        
        for i, num in enumerate(nums):
            if num != post + 1:
                answers.append([st, en])
                st = i
                en = i
            else:
                en += 1
            
            post = num
        
        answers.append([st, en])
        
        answer = []
        for (s, e) in answers[1:]:
            if s == e:
                answer.append(str(nums[s]))
            else:
                answer.append(f"{nums[s]}->{nums[e]}")
                
        return answer