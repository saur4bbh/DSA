class Solution:
    def myAtoi(self, s: str) -> int:
        left = False
        exempt = {' ','-','+'}
        ans = ''
        for i in s:
            if i.isdigit() == False and (left or i not in exempt):
                break
            elif i == '-' or i == '+' or i.isdigit():
                left = True
                ans += i

        if ans == '' or ans == '-' or ans == '+':
            ans = 0
        elif int(ans) < -2**31:
            ans = -2**31
        elif int(ans) > 2**31 - 1:
            ans = 2**31 - 1
        else:
            ans = int(ans)
        
        return ans

                

            
            
            