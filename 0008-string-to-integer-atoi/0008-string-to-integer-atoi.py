class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        ans = ''
        i = 0

        #step1
        while i<n and s[i] == ' ':
            i += 1
        
        #step2
        if i<n and s[i] in {'+','-'}:
            ans += s[i]
            i += 1

        #step3
        while i<n and s[i].isdigit():
            ans += s[i]
            i += 1

        #step4
        if ans in {'','+','-'}:
            return 0
        ans = max(-2**31, min(int(ans), 2**31 - 1))
        return ans




                

            
            
            