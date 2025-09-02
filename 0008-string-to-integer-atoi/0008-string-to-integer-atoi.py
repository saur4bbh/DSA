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
        elif i<n and not s[i].isdigit():
            return 0

        #step3
        while i<n and s[i].isdigit():
            ans += s[i]
            i += 1

        #step4
        if ans in {'','+','-'}:
            return 0
        elif int(ans) < -2**31:
            return -2**31
        elif int(ans) > 2**31 - 1:
            return 2**31 - 1
        else:
            return int(ans)




                

            
            
            