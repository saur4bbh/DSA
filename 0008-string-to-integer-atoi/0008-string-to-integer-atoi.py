class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        sign = 1
        ans = 0
        i = 0

        #step1
        while i<n and s[i] == ' ':
            i += 1
        
        #step2
        if i<n and s[i] in {'+','-'}:
            if s[i] == '-': sign = -1
            i += 1

        #step3
        while i<n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            ans = ans * 10 + digit
            i += 1

        #step4
        ans = max(-2**31, min(ans * sign, 2**31 - 1))
        return ans




                

            
            
            