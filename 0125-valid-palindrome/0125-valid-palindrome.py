# s <= 2 * 1e5
# O(N + N//2)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric chars and convert to lowercase letters
        s_lis = []
        for i in s:
            if i.isalpha():
                s_lis.append(i.lower())
            elif i.isdigit():
                s_lis.append(i)
        
        # palindrome check
        answer = True
        for i, c in enumerate(s_lis[:(len(s_lis) + 1)//2]):
            if c != s_lis[-(i + 1)]:
                answer = False
                break
        
        return answer
            