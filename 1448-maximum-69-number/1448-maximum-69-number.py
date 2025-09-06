class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = 0
        while num != 0:
            nums = nums*10 + num%10
            num //= 10
        
        ans = 0 
        rep = False
        while nums != 0:
            digit = nums%10
            if not rep and digit == 6:
                rep = True
                digit = 9
            ans = ans*10 + digit
            nums //= 10

        return ans
