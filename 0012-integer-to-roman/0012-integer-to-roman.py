# num <= 4 * 10**3

class Solution:
    def intToRoman(self, num: int) -> str:
        number_of_syms = []

        for i, val in enumerate([1000, 500, 100, 50, 10, 5, 1]):
            number_of_sym = num//val
            if number_of_sym == 4:
                if number_of_syms[i - 1] == 0:
                    number_of_sym = -1
                else:
                    number_of_syms[i - 1] = 0
                    number_of_sym = -2
            number_of_syms.append(number_of_sym)
            num = num%val
        
        answer = ""
        symbols = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        for i, n in enumerate(number_of_syms):
            if n >= 0:
                answer += symbols[i]*n
            elif n == -1:
                answer += symbols[i] + symbols[i - 1]
            else:
                answer += symbols[i] + symbols[i - 2]
        return answer
